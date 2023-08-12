from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modele.models import Modele

from users.models import Proprietaire
from .models import Voiture
from .serializers import *

# Définition de la classe pour la méthode GET (Get All)
class VoitureListAPIView(APIView):
    #Methode pour recupérer toutes les voitures ajoutées
    def get(self, request):
        try: 
            voitures = Voiture.objects.all()
            serializer = VoitureResponseSerializer(voitures, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Aucune voiture n'a été trouvée."}, status=status.HTTP_404_NOT_FOUND)
        
# Définition de la classe pour recupérer les voitures d'un propriétaire
class VoitureListProprietaireAPIView(APIView):
    # Méthode POST pour recupérer les voitures d'un propriétaire
    def get(self, request, proprietaire_id):
        print(proprietaire_id)
        try:
            voitures = Voiture.objects.filter(proprietaire=proprietaire_id)
        except Voiture.DoesNotExist:
            return Response(
                {"error": "Aucune voiture trouvée pour ce propriétaire."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = VoitureResponseSerializer(voitures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Définition de la classe pour la méthode POST (Create)
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
            response_serializer = VoitureResponseSerializer(instance)

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

# Définition de la classe pour la méthode GET (Get One)
class VoitureDetailAPIView(APIView):
    #Méthode pour recupérer les détails d'une voiture
    def get(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            serializer = VoitureResponseSerializer(voiture)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)

# Définition d'une classe pour la méthode PUT (Update)
class VoitureUpdateAPIView(APIView):
    #Méthode pour modifier les détails d'une voiture
    def put(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            serializer = VoitureSerializer(voiture, data=request.data)
            if serializer.is_valid():
                serializer.save()

                instance = Voiture.objects.get(numeroSerie=serializer.data.get('numeroSerie'))
                response_serializer = VoitureResponseSerializer(instance)

                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "Voiture not found."}, status=status.HTTP_404_NOT_FOUND)
        
# Définition de la classe pour la méthode DELETE
class VoitureDeleteAPIView(APIView):
    # Méthode pour supprimer une voiture
    def delete(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            if voiture.statutVoiture:  # Vérification du statut de la voiture
                return Response({"error": "Impossible de supprimer cette voiture car lié à une réservation."},
                                status=status.HTTP_403_FORBIDDEN)
            else:
                voiture.delete()
                return Response({"success": "Voiture supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)
                
        except Voiture.DoesNotExist:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)

# Définition de la classe pour rechercher une voiture en fonction de sa marque
class RechercheVoitureParMarqueAPIView(APIView):
    #Méthode pour rechercher une voiture en fonction de sa marque
    def get(self, request, marque):
        try:
            voitures = Voiture.objects.filter(modele__marque__nom__icontains=marque)
            serializer = VoitureResponseSerializer(voitures, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Voiture.DoesNotExist:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)
