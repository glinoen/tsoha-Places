from application import db
from application.models import Base

class Place(Base):
    name = db.Column(db.String(20), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=True)
    topics = db.relationship('Topic', backref='place', lazy=True)

    children = db.relationship("Place")
    
    def __init__(self, name, parent_id):
        self.name = name
        self.parent_id = parent_id
