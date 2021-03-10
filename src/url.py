from flask import Blueprint

from .views.item import item
from .views.flavor import flavor
from .views.client import client
from .views.orders import orders

v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

v1.add_url_rule('/item', view_func=item, methods=['GET', 'POST'])
v1.add_url_rule('/item/<int:pk>', view_func=item, methods=['PUT', 'DELETE'])

v1.add_url_rule('/flavor', view_func=flavor, methods=['GET', 'POST'])
v1.add_url_rule('/flavor/<int:pk>', view_func=flavor, methods=['PUT', 'DELETE'])

v1.add_url_rule('/client', view_func=client, methods=['GET', 'POST'])
v1.add_url_rule('/client/<int:pk>', view_func=client, methods=['PUT', 'DELETE'])

v1.add_url_rule('/orders', view_func=orders, methods=['GET', 'POST'])
v1.add_url_rule('/orders/<int:pk>', view_func=orders, methods=['PUT', 'DELETE'])
