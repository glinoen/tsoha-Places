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

