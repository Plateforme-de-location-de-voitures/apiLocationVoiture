from django.urls import path
from .views import *

urlpatterns = [
    path('voitures', VoitureListAPIView.as_view(), name='voiture_list'),
    path('voiture/<int:pk>', VoitureDetailAPIView.as_view(), name='voiture_detail'),
    path('recherche/voitures-par-marque/<str:marque>', RechercheVoitureParMarqueAPIView.as_view(), name='recherche-voitures-par-marque'),
    path('voiture/create', VoitureCreateAPIView.as_view(), name='voiture_create'),
    path('voiture/update/<int:pk>', VoitureUpdateAPIView.as_view(), name='voiture_update'),
    path('voiture/delete/<int:pk>', VoitureDeleteAPIView.as_view(), name='voiture_delete'),
]