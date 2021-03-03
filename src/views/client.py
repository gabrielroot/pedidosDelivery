import json
import datetime
from flask import jsonify, request
from flask.views import MethodView
from src.models import Client
from src.schema.client import ClientSchema


class ClientView(MethodView):
    schema = ClientSchema()

    def get(self):
        clients = Client.query.filter_by(deleted_at=None).all()
        data = self.schema.dump(clients, many=True)
        return jsonify(data), 200

    def post(self):
        req = json.loads(request.data)
        client = Client()

        if 'name' in req and 'password' in req and 'email' in req:
            client.name = req['name']
            client.password = req['password']
            client.email = req['email']
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

        client.save()
        data = self.schema.dump(client)
        return jsonify(data), 200

    def delete(self, pk):
        client = Client.query.filter_by(id=pk).first_or_404(description='Client not found')
        client.deleted_at = datetime.datetime.utcnow()
        client.save()
        return jsonify({}), 203


client = ClientView.as_view('client')
