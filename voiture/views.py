from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modele.models import Modele

from users.models import Proprietaire
from .models import Voiture
from .serializers import *

# Définition d'une classe pour la méthode GET (Get All)
class VoitureListAPIView(APIView):
    
    def get(self, request):
        voitures = Voiture.objects.all()
        serializer = VoitureSerializer(voitures, many=True)
        return Response(serializer.data)

# Définition d'une classe pour la méthode POST (Create)
class VoitureCreateAPIView(APIView):
    # Méthode POST pour créer une nouvelle instance de Voiture
    def post(self, request):
        # proprietaire_id = request.data.get('proprietaire')
        # modele_id = request.data.get('modele')
        # numeroSerie = request.data.get('numeroSerie')
        # vinNumber = request.data.get('vinNumber')
        # couleur = request.data.get('couleur')
        # prix = request.data.get('prix')
        # anneeFabrication = request.data.get('anneeFabrication')
        # puissance = request.data.get('puissance')
        # imagePrincipal = request.data.get('imagePrincipal')
        # statutVoiture = request.data.get('statutVoiture')
        serializer = VoitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            instance = Voiture.objects.get(numeroSerie=serializer.data.get('numeroSerie'))
            response_serializer = VoitureSerializer(instance)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        # try:
        #     proprietaire = Proprietaire.objects.get(id=proprietaire_id)
        #     modele = Modele.objects.get(id=modele_id)
        #     Voiture.objects.create(proprietaire=proprietaire, modele=modele, numeroSerie=numeroSerie,
        #         vinNumber=vinNumber, couleur= couleur, prix=prix, anneeFabrication=anneeFabrication,
        #         puissance=puissance, imagePrincipal=imagePrincipal, statutVoiture=statutVoiture)
            
        # except Proprietaire.DoesNotExist or Modele.DoesNotExist:
        #     return Response({"message": "Le modèle et le propriétaire n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
        
        # return Response({"message": "Voiture ajoutée avec succès"}, status=status.HTTP_201_CREATED)

# Définition d'une classe pour la méthode GET (Get One)
class VoitureDetailAPIView(APIView):
    
    def get(self, request, pk):
        voiture = Voiture.objects.get(pk=pk)
        serializer = VoitureSerializer(voiture)
        return Response(serializer.data)

# Définition d'une classe pour la méthode PUT (Update)
class VoitureUpdateAPIView(APIView):

    def put(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            serializer = VoitureSerializer(voiture, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                response_serializer = VoitureSerializer(voiture)

                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "Voiture not found."}, status=status.HTTP_404_NOT_FOUND)
        
# Définition d'une classe pour la méthode DELETE
class VoitureDeleteAPIView(APIView):

    def delete(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            voiture.delete()  
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"detail": "Voiture not found."}, status=status.HTTP_404_NOT_FOUND)
