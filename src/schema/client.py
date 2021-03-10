from src import ma
from src.models import Client
from src.models import FlavorItems
from marshmallow import fields


class OrdersSchema(ma.Schema):

    class Meta:
        model = FlavorItems
        fields = ('item_id', 'flavor_id')


class ClientSchema(ma.Schema):
    orders = fields.Nested(OrdersSchema, many=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'street', 'district', 'number', 'orders', 'created_at', 'updated_at')
        ordered = True
