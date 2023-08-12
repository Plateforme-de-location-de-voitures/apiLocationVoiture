from rest_framework import serializers
from marque.serializers import MarqueSerializer

from modele.models import Modele

class ModeleSerializer(serializers.ModelSerializer):

    class Meta:
       
        model = Modele
        fields = '__all__'

class ModeleResponseSerializer(serializers.ModelSerializer):
    marque = MarqueSerializer()
    class Meta:
       
        model = Modele
        fields = '__all__'
