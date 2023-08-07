# Importation des modules nécessaires
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
    # Méthode GET pour récupérer toutes les instances de Voiture
    def get(self, request):
        try: 
            voitures = Voiture.objects.all()
            serializer = VoitureSerializer(voitures, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Aucune voiture n'a été trouvée."}, status=status.HTTP_404_NOT_FOUND)

# Définition d'une classe pour la méthode POST (Create)
class VoitureCreateAPIView(APIView):
    # Méthode POST pour créer une nouvelle instance de Voiture
    def post(self, request):
        serializer = VoitureSerializer(data=request.data)  # Crée une instance du sérialiseur VoitureSerializer avec les données reçues en tant que paramètre.
        if serializer.is_valid():  # Vérifie si les données fournies sont valides en fonction des règles de validation définies dans VoitureSerializer.
            serializer.save()  # Sauvegarde l'instance de Voiture dans la base de données.

            # Récupérer l'instance de Voiture ajoutée depuis la base de données en fonction du numero de voiture envoyé dans la réponse
            instance = Voiture.objects.get(numero=serializer.data.get('numeroSerie'))
            response_serializer = VoitureResponseSerializer(instance)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)  # Renvoie les données sérialisées sous forme de réponse HTTP avec le code de statut 201 (Créé).

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Renvoie les erreurs de validation sous forme de réponse HTTP avec le code de statut 400 (Bad Request).

# Définition d'une classe pour la méthode GET (Get One)
class VoitureDetailAPIView(APIView):
    
    def get(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            serializer = VoitureSerializer(voiture)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)
# Définition d'une classe pour la méthode PUT (Update)
class VoitureUpdateAPIView(APIView):
    # Méthode PUT pour mettre à jour une instance de Voiture spécifique en fonction de son ID (pk)
    def put(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk) # Récupère une instance de Voiture en fonction de son ID (pk) depuis la base de données.
            serializer = VoitureSerializer(voiture, data=request.data)  # Sérialise l'instance de Voiture avec les nouvelles données fournies en tant que paramètre.
            if serializer.is_valid():  # Vérifie si les données fournies sont valides en fonction des règles de validation définies dans VoitureSerializer.
                serializer.save()  # Sauvegarde les modifications de l'instance de Voiture dans la base de données.
                
                # Récupérer l'instance de Voiture modifiée depuis la base de données en fonction de l'id dans la réponse
                response_serializer = VoitureResponseSerializer(voiture)

                return Response(response_serializer.data, status=status.HTTP_201_CREATED)  # Renvoie les données sérialisées sous forme de réponse HTTP avec le code de statut 201 (Créé).

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Renvoie les erreurs de validation sous forme de réponse HTTP avec le code de statut 400 (Bad Request).
        except:
            return Response({"detail": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)
        
# Définition d'une classe pour la méthode DELETE
class VoitureDeleteAPIView(APIView):
    # Méthode DELETE pour supprimer une instance spécifique de Voiture en fonction de son ID (pk)
    def delete(self, request, pk):
        try:
            voiture = Voiture.objects.get(pk=pk)
            if voiture.statutVoiture:  # Vérification du statut de la voiture
                voiture.delete()
                return Response({"success": "Voiture supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Impossible de supprimer cette voiture car lié à une réservation."},
                                status=status.HTTP_403_FORBIDDEN)
        except Voiture.DoesNotExist:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)
        

# Définition de la classe pour rechercher une voiture en fonction de sa marque
class RechercheVoitureParMarqueAPIView(APIView):
    #Méthode pour rechercher une voiture en fonction de sa marque
    def get(self, request, marque):
        try:
            voitures = Voiture.objects.filter(modele__marque__nom__icontains=marque)
            serializer = VoitureSerializer(voitures, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Voiture.DoesNotExist:
            return Response({"error": "Voiture non trouvée."}, status=status.HTTP_404_NOT_FOUND)
        
# Définition de la classe pour recupérer les voitures d'un propriétaire
class VoitureListProprietaireAPIView(APIView):
    # Méthode POST pour recupérer les voitures d'un propriétaire
    def get(self, request, proprietaire_id):
        try:
            voitures = Voiture.objects.filter(proprietaire=proprietaire_id)
        except Voiture.DoesNotExist:
            return Response(
                {"error": "Aucune voiture trouvée pour ce propriétaire."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = VoitureSerializer(voitures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
