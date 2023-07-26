from rest_framework import serializers

from marque.models import Marque

class MarqueSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Marque
        fields = '__all__'
    

