from django.urls import path
from api.views import DealView

urlpatterns = [
    path('messages/', DealView.as_view({'get': 'list'})),
]
