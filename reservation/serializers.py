from rest_framework import serializers
from reservation.models import Reservation
from users.serializers import PersonneResponseSerializer
from voiture.serializers import VoitureResponseSerializer

class ReservationSerializer(serializers.ModelSerializer):

    #dateReservation = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    #dateRetour = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
       
        model = Reservation
       
        fields = '__all__'

class ReservationResponseSerializer(serializers.ModelSerializer):

    client = PersonneResponseSerializer()
    voiture = VoitureResponseSerializer()
    #dateReservation = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    #dateRetour = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
       
        model = Reservation
       
        fields = '__all__'