from flask import jsonify
from flask.views import MethodView
from src.models import Item
from src.schema.item import ItemSchema


class ItemView(MethodView):
    schema = ItemSchema()

    def get(self):
        items = Item.query.filter_by(deleted_at=None).all()
        data = self.schema.dump(items, many=True)
        return jsonify(data), 200


item = ItemView.as_view('item')
