from flask import Blueprint

from .views.item import item
from .views.flavor import flavor

v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

v1.add_url_rule('/item', view_func=item, methods=['GET'])
v1.add_url_rule('/flavor', view_func=flavor, methods=['GET'])
