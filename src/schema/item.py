from src import ma
from src.models import Item
from src.models import Flavor
from marshmallow import fields


class ItemFlavorSchema(ma.Schema):

    class Meta:
        model = Flavor
        fields = ('name', 'available')


class ItemSchema(ma.Schema):
    flavors = fields.Nested(ItemFlavorSchema, many=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'flavors', 'description', 'available', 'created_at', 'updated_at')
        ordered = True
