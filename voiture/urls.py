from django.urls import path
from .views import *

urlpatterns = [
    path('voitures', VoitureListAPIView.as_view(), name='voiture_list'),
    path('voiture/create', VoitureCreateAPIView.as_view(), name='voiture_create'),
    path('voiture/<int:pk>', VoitureDetailAPIView.as_view(), name='voiture_detail'),
    path('voiture/update/<int:pk>', VoitureUpdateAPIView.as_view(), name='voiture_update'),
    path('voiture/delete/<int:pk>', VoitureDeleteAPIView.as_view(), name='voiture_delete'),
]