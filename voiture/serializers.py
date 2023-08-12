from rest_framework import serializers

from modele.serializers import ModeleResponseSerializer
from users.serializers import PersonneResponseSerializer
from .models import  Voiture

class VoitureSerializer(serializers.ModelSerializer):
    # Configuration du serializer
    class Meta:
        # Le modèle sur lequel se base le serializer est Voiture
        model = Voiture
        # Le serializer inclut toutes les propriétés (champs) du modèle Voiture
        fields = '__all__'

class VoitureResponseSerializer(serializers.ModelSerializer):
    # Configuration du serializer
    modele = ModeleResponseSerializer()
    proprietaire = PersonneResponseSerializer()
    class Meta:
        # Le modèle sur lequel se base le serializer est Voiture
        model = Voiture
        # Le serializer inclut toutes les propriétés (champs) du modèle Voiture
        fields = '__all__'