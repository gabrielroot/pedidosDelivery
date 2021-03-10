import json
import datetime
from src.models import Item
from src.models import Flavor
from sqlalchemy import engine
from src.models import Orders
from flask import jsonify, request
from flask.views import MethodView
from src.schema.orders import OrdersSchema


class ClientView(MethodView):
    schema = OrdersSchema()

    def get(self):
        orders = Orders.query.filter_by(deleted_at=None).all()
        data = self.schema.dump(orders, many=True)
        return jsonify(data), 200


orders = ClientView.as_view('orders')
