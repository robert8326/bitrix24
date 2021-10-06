from rest_framework import serializers

from api.models import Deal
from api.serializers.contact import ClientSerializer
from api.serializers.product import ProductSerializer


class DealSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Deal
        exclude = ('id',)
