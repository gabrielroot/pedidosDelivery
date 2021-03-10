import json
import datetime
from src.models import Item
from src.models import Flavor
from flask import jsonify, request
from flask.views import MethodView
from src.schema.item import ItemSchema


class ItemView(MethodView):
    schema = ItemSchema()

    def get(self):
        items = Item.query.filter(Item.deleted_at==None).all()
        data = self.schema.dump(items, many=True)
        return jsonify(data), 200

    def post(self):
        req = json.loads(request.data)
        item = Item()

        if 'name' not in req or 'available' not in req or 'price' not in req or 'flavors' not in req:
            return jsonify({"message": "Body is invalid"})

        if 'name' in req and 'price' in req:
                item.name = req['name']
                item.price = req['price']
        else:
            return jsonify({"message": "Body is invalid"})

        if 'available' in req:
            item.available = req['available']

        if 'description' in req:
            item.description = req['description']

        if 'flavors' in req and type(req['flavors']) == list:
            for flavor in req['flavors']:
                exists = Flavor.query.filter_by(name=flavor['name']).first()
                if not exists:
                    if 'name' in flavor:
                        insert = Flavor()
                        insert.name = flavor['name']
                        item.flavors.append(insert)
                        insert.save()
                else:
                    item.flavors.append(exists)

        item.save()
        data = self.schema.dump(item)
        return jsonify(data), 201

    def put(self, pk):

        item = Item.query.filter_by(id=pk).first_or_404(description='Item not found')
        req = json.loads(request.data)

        if 'name' not in req and 'available' not in req and 'price' not in req and \
           'description' not in req and 'flavors' not in req:
            return jsonify({"message": "Body is invalid"})

        if 'name' in req:
            item.name = req['name']

        if 'available' in req:
            item.available = req['available']

        if 'price' in req:
            item.price = req['price']

        if 'description' in req:
            item.description = req['description']

        if 'flavors' in req and type(req['flavors']) == list:
            for flavor in req['flavors']:
                if 'name' in flavor:
                    exists = Flavor.query.filter_by(name=flavor['name']).first()
                    if not exists:
                        insert = Flavor()
                        insert.name = flavor['name']
                        insert.save()
                        item.flavors.append(insert)
                    else:
                        exists.name = flavor['name']
                        if 'available' in flavor:
                            exists.available = flavor['available']
                        exists.save()
                        item.flavors.append(exists)

        item.save()
        data = self.schema.dump(item)
        return jsonify(data), 200

    def delete(self, pk):

        item = Item.query.filter_by(id=pk, deleted_at=None).first_or_404(description='Item not found')
        item.deleted_at = datetime.datetime.utcnow()
        item.save()
        return jsonify({}), 203


item = ItemView.as_view('item')
