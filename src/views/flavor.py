import json
import datetime
from flask import jsonify, request
from flask.views import MethodView

from src.models import Flavor
from src.schema.flavor import FlavorSchema


class FlavorView(MethodView):
    schema = FlavorSchema()

    def get(self):

        flavors = Flavor.query.filter_by(deleted_at=None).all()
        data = self.schema.dump(flavors, many=True)
        return jsonify(data), 200

    def post(self):

        req = json.loads(request.data)
        flavor = Flavor()

        if 'name' in req:
            flavor.name = req['name']
        else:
            return jsonify({"message": "Body is invalid"})

        flavor.save()
        data = self.schema.dump(flavor)
        return jsonify(data), 201

    def put(self, pk):
        data = json.loads(request.data)
        flavor = Flavor.query.filter_by(id=pk).first_or_404(description='Flavor not found')

        if 'name' in data:
            flavor.name = data['name']

        if 'available' in data:
            flavor.available = data['available']

        flavor.save()
        data = self.schema.dump(flavor)
        return jsonify(data), 200

    def delete(self, pk):

        flavor = Flavor.query.filter_by(id=pk, deleted_at=None).first_or_404(description='Flavor not found')
        flavor.deleted_at = datetime.datetime.utcnow()
        flavor.save()
        return jsonify({}), 203


flavor = FlavorView.as_view('flavor')
