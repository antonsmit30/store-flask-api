from flask_jwt import JWT
from db import db

class ItemModel(db.Model):


    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    # List of items - Many to One
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()


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





