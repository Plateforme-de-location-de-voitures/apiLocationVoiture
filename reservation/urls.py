from django.urls import path
from .views import *

urlpatterns = [
    path('reservations', ReservationListAPIView.as_view(), name='reservations_list'),
    path('reservation/create', ReservationCreateAPIView.as_view(), name='reservation_create'),
    path('reservation/recherche/<str:nom_client>', ReservationRechercheAPIView.as_view(), name='reservation_search'),
    path('reservation/update/<int:reservation_id>/', ReservationUpdateAPIView.as_view(), name='reservation_update'),
    path('reservation/delete/<int:reservation_id>/', ReservationDeleteAPIView.as_view(), name='reservation_delete'),
    path('reservation/detail/<int:reservation_id>/', ReservationDetailAPIView.as_view(), name='reservation_detail'),
    path('fin/<int:reservation_id>/', FinDuneReservationAPIView.as_view(), name='reservation_fin'),
    path('voiture/disponible/<str:date_reservation>/<str:date_retour>/', RechercheDesVoituresEntreDeuxDatesAPIView.as_view(), name='reservation_voiture_disponible')
]