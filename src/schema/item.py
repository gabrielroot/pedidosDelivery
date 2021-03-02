from src import ma
from src.models import Item


class ItemSchema(ma.Schema):

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'available', 'created_at', 'updated_at')
