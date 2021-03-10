from src import ma
from src.models import Orders


class OrdersSchema(ma.Schema):

    class Meta:

        model = Orders
        fields = ('id', 'flavorItem_id', 'client_id', 'quantity', 'observation', 'created_at', 'updated_at')
