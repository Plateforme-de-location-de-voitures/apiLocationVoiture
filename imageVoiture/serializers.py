from rest_framework import serializers
from .models import ImageVoiture

class ImageVoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageVoiture
        fields = '__all__'
