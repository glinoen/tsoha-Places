from application import db
from application.models import Base
from application.auth.models import User
from sqlalchemy.sql import text

topicAccount = db.Table('topic_account',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
)


class Topic(Base):
    
    messages = db.relationship('Message', backref='topic', lazy=True)
    accounts = db.relationship('User', secondary=topicAccount, backref = db.backref("topics", lazy="dynamic"), lazy="dynamic")

    name = db.Column(db.String(100), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    
    def __init__(self, name,place_id):
            self.name = name
            self.place_id = place_id



    @staticmethod
    def latest():
        stmt = text("SELECT Topic.id, MAX(Message.date_created) FROM Message"
                    " LEFT JOIN Topic ON Topic.id = Message.topic_id"
                    " GROUP BY Topic.id, Message.date_created"
                    " ORDER BY Message.date_created DESC")
        res = db.engine.execute(stmt)



        response = []
        for row in res:
            response.append({"topic_id":row[0], "date_created":row[1]})

        return response
    
    @staticmethod
    def replycount():
        stmt = text('SELECT Topic.id, COUNT(Message.topic_id) as count FROM Topic'
                    ' INNER JOIN Message ON Topic.id = Message.topic_id'
                    ' GROUP BY Topic.id'
                    ' ORDER BY count DESC')
        res = db.engine.execute(stmt)

        table = []
        for row in res:
            table.append({"topic_id":row[0], "replies":row[1]})

        return table    