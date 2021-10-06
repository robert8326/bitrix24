from django.urls import path
from api.views import DealView

urlpatterns = [
    path('deal/', DealView.as_view({'post': 'create', 'get': 'list'})),
]
