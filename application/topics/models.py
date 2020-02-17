from application import db
from application.models import Base

class Topic(Base):
    
    messages = db.relationship('Message', backref='topic', lazy=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    name = db.Column(db.String(100), nullable=False)
    #place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    
    def __init__(self, name, account_id):
            self.name = name
            self.account_id = account_id

