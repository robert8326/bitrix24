from rest_framework import viewsets
from api.models import Deal
from api.serializers import DealSerializer


class DealView(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    http_method_name = ['post', 'get']

    # def list(self, request, *args, **kwargs):
    #     pass
