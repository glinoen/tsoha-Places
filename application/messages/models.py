from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #topic
    #parent_message_id
    
    content = db.Column(db.String(500), nullable=False)

    def __init__(self, content):
        self.content = content
        self.done = False