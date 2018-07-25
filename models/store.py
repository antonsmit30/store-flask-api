from flask_jwt import JWT
from db import db

class StoreModel(db.Model):


    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')


    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def save_to_db(self):
        # SQL alchemy add to database
        db.session.add(self)
        db.session.commit()

    # Delete our item
    def delete_from_db(self, name):
        db.session.delete(self)
        db.session.commit()

    #Print
    def __str__(self):
        return 'name : {} \nprice: {}'.format(self.name, self.price)