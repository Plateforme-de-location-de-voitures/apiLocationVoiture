from rest_framework import serializers
from .models import  Voiture

class VoitureSerializer(serializers.ModelSerializer):
    # Configuration du serializer
    class Meta:
        # Le modèle sur lequel se base le serializer est Voiture
        model = Voiture
        # Le serializer inclut toutes les propriétés (champs) du modèle Voiture
        fields = '__all__'