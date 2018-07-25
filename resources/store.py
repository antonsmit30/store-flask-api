from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):

    # only retrieve store
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'Message ': 'Store not found'}, 404

    def post(self, name):
        # If store exists return message it exists
        if StoreModel.find_by_name(name):
            return {"Message ": "Store {} exists".format(name)}, 400

        # Else create store
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return{'message'" 'internal server error"}, 500
        return store.json(), 201

    def delete(self, name):

        #Look for store. If it exists, delete it.
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db(name)

        return {'message': 'Store deleted'}

class StoreList(Resource):
    #return list of stores
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
