from src import ma
from src.models import Client


class ItemSchema(ma.Schema):

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'created_at', 'updated_at')
