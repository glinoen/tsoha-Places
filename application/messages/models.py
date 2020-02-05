from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    #parent_message_id
    
    content = db.Column(db.String(500), nullable=False)

    def __init__(self, content, topic_id, account_id):
        self.content = content
        self.topic_id = topic_id
        self.account_id = account_id