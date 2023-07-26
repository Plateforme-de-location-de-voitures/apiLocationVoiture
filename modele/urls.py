
from django.urls import path
from .views import *

urlpatterns = [
    path('modeles', ModeleListAPIView.as_view(), name='modeles_list'),
    path('modele/create', ModeleCreateAPIView.as_view(), name='modele_create'),
    path('modele/update/<int:modele_id>', ModeleUpdateAPIView.as_view(), name='modele_update'),
    path('modele/delete/<int:modele_id>', ModeleDeleteAPIView.as_view(), name='modele_delete'),
]
