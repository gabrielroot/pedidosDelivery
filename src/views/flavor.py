from flask import Flask, jsonify
from flask.views import MethodView

from src.models import Flavor
from src.schema.flavor import FlavorSchema

class FlavorView(MethodView):
    schema = FlavorSchema()

    def get(self):
        flavors = Flavor.query.filter_by(deleted_at=None).all()
        data = self.schema.dump(flavors, many=True)
        return jsonify(data), 200
    

flavor = FlavorView.as_view('flavor')