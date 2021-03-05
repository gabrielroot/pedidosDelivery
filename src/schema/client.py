from src import ma
from src.models import Client


class ClientSchema(ma.Schema):

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'street', 'district', 'number', 'created_at', 'updated_at')
