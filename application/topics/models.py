from application import db

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    messages = db.relationship('Message', backref='topic', lazy=True)
    
    name = db.Column(db.String(144), nullable=False)
    #place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    
    def __init__(self, name):
            self.name = name
            self.done = False

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    #parent_message_id
    
    content = db.Column(db.String(500), nullable=False)

    def __init__(self, content, topic_id):
        self.content = content
        self.topic_id = topic_id
        