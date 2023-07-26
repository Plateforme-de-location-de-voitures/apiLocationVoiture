from rest_framework import serializers

from modele.models import Modele

class ModeleSerializer(serializers.ModelSerializer):

    class Meta:
       
        model = Modele
        fields = '__all__'

