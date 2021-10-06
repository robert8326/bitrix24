from rest_framework import serializers

from api.models import Deal
from api.serializers.contact import ClientSerializer


class DealSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Deal
        exclude = ('id',)
