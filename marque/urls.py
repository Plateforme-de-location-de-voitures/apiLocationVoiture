from django.urls import path
from .views import *

urlpatterns = [
    path('marques', MarqueListAPIView.as_view(), name='marques_list'),
    path('marque/create', MarqueCreateAPIView.as_view(), name='marque_create'),
    path('marque/update/<int:marque_id>', MarqueUpdateAPIView.as_view(), name='marque_update'),
    path('marque/delete/<int:marque_id>', MarqueDeleteAPIView.as_view(), name='marque_delete'),
]
