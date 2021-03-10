import json
import datetime
from src.models import Client
from src.models import Item
from src.models import Orders
from flask import jsonify, request
from flask.views import MethodView
from src.schema.client import ClientSchema


class ClientView(MethodView):
    schema = ClientSchema()

    def get(self):
        clients = Client.query.filter(Client.deleted_at==None).all()
        print(clients[1].orders)
        print(Client.query.join(Client.orders).filter_by(item_id=Item.id).all())
        data = self.schema.dump(clients, many=True)
        return jsonify(data), 200

    def post(self):
        req = json.loads(request.data)
        client = Client()

        if 'name' in req and 'password' in req and 'email' in req and 'street' in req \
           and 'district' in req and 'number' in req:
            client.name = req['name']
            client.password = req['password']
            client.email = req['email']
            client.street = req['street']
            client.district = req['district']
            client.name = req['name']
        else:
            return jsonify({"message": "Body is invalid"})

        client.save()
        data = self.schema.dump(client)
        return jsonify(data), 201

    def put(self, pk):
        client = Client.query.filter_by(id=pk).first_or_404(description='Client not found')
        req = json.loads(request.data)

        if 'name' not in req and 'email' not in req and 'password' not in req:
            return jsonify({"message": "Body is invlid"})

        if 'name' in req:
            client.name = req['name']

        if 'email' in req:
            client.email = req['email']

        if 'password' in req:
            client.password = req['password']

        if 'street' in req:
            client.street = req['street']

        if 'district' in req:
            client.district = req['district']

        if 'number' in req:
            client.number = req['number']
        

        client.save()
        data = self.schema.dump(client)
        return jsonify(data), 200

    def delete(self, pk):
        client = Client.query.filter_by(id=pk, deleted_at=None).first_or_404(description='Client not found')
        client.deleted_at = datetime.datetime.utcnow()
        client.save()
        return jsonify({}), 203


client = ClientView.as_view('client')
