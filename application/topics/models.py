from application import db
from application.models import Base
from sqlalchemy.sql import text

class Topic(Base):
    
    messages = db.relationship('Message', backref='topic', lazy=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    name = db.Column(db.String(100), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    
    def __init__(self, name, account_id, place_id):
            self.name = name
            self.account_id = account_id
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