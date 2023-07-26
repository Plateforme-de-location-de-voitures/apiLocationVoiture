from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from voiture.models import Voiture
from .models import ImageVoiture
from .serializers import ImageVoitureSerializer
from django.shortcuts import get_object_or_404

#fonction pour afficher la liste des images
class ImageVoitureListAPIView(APIView):
    def get(self, request):
        images = ImageVoiture.objects.all()
        serializer = ImageVoitureSerializer(images, many=True)
        return Response(serializer.data)
    
#fonction pour afficher les détails d'une image
class ImageDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(ImageVoiture, pk=pk)

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageVoitureSerializer(image)
        return Response(serializer.data)

#fonction pour afficher les images associé a  une voiture en fonction de son id  
class ImageParVoitureAPIView(APIView):   
    def get(self, request, voiture_id):
        try:
            voiture = Voiture.objects.get(id=voiture_id)
            images = ImageVoiture.objects.filter(voiture=voiture)
            serializer = ImageVoitureSerializer(images, many=True)
            return Response(serializer.data)
        except Voiture.DoesNotExist:
            return Response({"error": "La voiture n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
        
#fonction pour l'ajout d'une image en fonction de l'id d'une voiture
class ImageVoitureCreateAPIView(APIView):
    def post(self, request):
        voiture_id = request.data.get('voiture')
        images = request.FILES.getlist('images')
        
        try:
            voiture = Voiture.objects.get(id=voiture_id)
        except Voiture.DoesNotExist:
            return Response({"error": "La voiture n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
        
        for image in images:
            ImageVoiture.objects.create(voiture=voiture, image=image)
        
        # Sérialiser les instances d'ImageVoiture créées
        images_serializer = ImageVoitureSerializer(voiture.images.all(), many=True)
        
        return Response(images_serializer.data, status=status.HTTP_201_CREATED)

#fonction pour supprimer une voiture  
class ImageVoitureDeleteAPIView(APIView):

    def delete(self, request, pk):
        try:
            image_voiture = ImageVoiture.objects.get(pk=pk)
            image_voiture.delete()
            return Response({"success": "Image supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except ImageVoiture.DoesNotExist:
            return Response({"error": "L'image spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)