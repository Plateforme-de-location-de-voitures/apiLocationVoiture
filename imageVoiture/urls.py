from django.contrib import admin
from django.urls import path
from imageVoiture.views import *

urlpatterns = [
    path('images/voitures', ImageVoitureListAPIView.as_view(), name='image_voiture_list'),
    path('images/voiture/<int:voiture_id>', ImageParVoitureAPIView.as_view(), name='images_par_voiture'),
    path('image/voiture/create', ImageVoitureCreateAPIView.as_view(), name='image_voiture_create'),
    path('image/voiture/<int:pk>', ImageDetailAPIView.as_view(), name='image_voiture_detail'),
    path('image/voiture/delete/<int:pk>', ImageVoitureDeleteAPIView.as_view(), name='image_voiture_delete'), 
]
