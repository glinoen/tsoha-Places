from application import db
from application.models import Base

class Topic(Base):
    
    messages = db.relationship('Message', backref='topic', lazy=True)
    
    name = db.Column(db.String(144), nullable=False)
    #place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    
    def __init__(self, name):
            self.name = name
            self.done = False

