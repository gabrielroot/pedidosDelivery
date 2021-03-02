from src import ma
from src.models import Flavor


class FlavorSchema(ma.Schema):

    class Meta:
        model = Flavor
        fields = ('id', 'name', 'available', 'created_at', 'updated_at')
