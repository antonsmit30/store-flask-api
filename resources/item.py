from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        # If row exists
        if item:
            return item.json()
        # Else return error
        return{'message': 'Item not found'}


    # Create our item
    def post(self, name):
        if ItemModel.find_by_name(name):
            print(ItemModel.find_by_name(name))
            return {'message': 'An item with name {} already exists'.format(name)}, 400

        data = Item.parser.parse_args()
        print(data)
        print('Helo!')
        print(name)

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            print(item)
            item.save_to_db()
        except:
            return{'Message': 'an error ocured'}, 500 # Internal server error (not your fault)
        else:
            return {'Message': 'Item saved successfully.'}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db(name)
        return {'message': 'Item deleted'}


    # Update or Create
    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)


        if item:
            item.price = data['price']
        else:
            try:
                item = ItemModel(name, data['price'], data['store_id'])
            except:
                return {'Message': 'an error ocured'}, 500  # Internal server error (not your fault)

        item.save_to_db()
        return item.json()



class ItemList(Resource):
    def get(self):
        #return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}


