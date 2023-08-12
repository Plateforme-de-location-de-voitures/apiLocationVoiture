from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response  
from reservation.models import Reservation  
from voiture.models import Voiture
from reservation.serializers import  *  
from voiture.serializers import  VoitureSerializer  
import datetime
from django.utils import timezone

#Classe pour lister toutes les réservations
class ReservationListAPIView(APIView):
   
    def get(self, request):
        reservations = Reservation.objects.all()  
        serializer = ReservationResponseSerializer(reservations, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 

#Classe pour créer une réservation
class ReservationCreateAPIView(APIView):
   
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)  

        date_reservation = request.data.get('dateReservation')
        date_retour = request.data.get('dateRetour')

        if date_reservation >= date_retour:
            return Response(
                {"error": "La date de réservation doit être inférieure à la date de retour."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.is_valid():  
            serializer.save()

            instance = Reservation.objects.get(dateReservation=serializer.data.get('dateReservation'))
            response_serializer = ReservationResponseSerializer(instance)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe pour mettre à jour une réservation
class ReservationUpdateAPIView(APIView):
   
    def put(self, request, reservation_id):
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservationSerializer(reservation, data=request.data)

        date_reservation = request.data.get('dateReservation')
        date_retour = request.data.get('dateRetour')

        if date_reservation >= date_retour:
            return Response(
                {"error": "La date de réservation doit être inférieure à la date de retour."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.is_valid():
            serializer.save()

            instance = Reservation.objects.get(dateReservation=serializer.data.get('dateReservation'))
            response_serializer = ReservationResponseSerializer(instance)
            
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une réservation qui est terminée
class ReservationDeleteAPIView(APIView):

     def delete(self, request, reservation_id):
        try:
           
            reservation = Reservation.objects.get(pk=reservation_id)
        except Reservation.DoesNotExist:
            return Response({"error": "La réservation spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        if reservation.statutReservation == True:
            reservation.delete()
            return Response({"success": "Réservation supprimée avec succès."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Vous ne pouvez pas supprimer cette réservation car elle est 'en cours'."},
                            status=status.HTTP_400_BAD_REQUEST)


#Classe pour rechercher une réservation par le nom du client
class ReservationRechercheAPIView(APIView):

    def get(self, request, nom_client):

        reservations = Reservation.objects.all()

        if nom_client:
            # Si le nom du client est fourni, recherchez les réservations pour ce client
            reservations = reservations.filter(client__nom__icontains=nom_client)

        # Utilisez votre sérialiseur pour sérialiser les résultats
        serializer = ReservationResponseSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#Classe pour afficher les détails d'une réservation
class ReservationDetailAPIView(APIView):
    def get(self, request, reservation_id):
        try:
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "La réservation demandée n'existe pas."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationResponseSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)


#Classe pour trouver les voitures disponible lorsque l'utilisateur renseigne ses dates de réservation
class RechercheDesVoituresEntreDeuxDatesAPIView(APIView):

       def get(self, request, date_reservation, date_retour):
        if not date_reservation or not date_retour:
            return Response(
                {"error": "Veuillez fournir les dates de réservation et de retour."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if date_reservation >= date_retour:
            return Response(
                {"error": "La date de réservation doit être antérieure à la date de retour."},
                status=status.HTTP_400_BAD_REQUEST
            )

        reservations_chevauchantes = Reservation.objects.filter(
            dateReservation__lte= date_retour,
            dateRetour__gte=date_reservation
        )

        voitures_indisponibles = Voiture.objects.filter(reservation__in=reservations_chevauchantes)
        voitures_disponibles = Voiture.objects.filter(statutVoiture =False).exclude(id__in=voitures_indisponibles)

        serializer = VoitureResponseSerializer(voitures_disponibles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Classe pour enregistrer la fin d'un réservation
class FinDuneReservationAPIView(APIView):
    
    def put(self, request, *args, **kwargs):

        reservation_id = kwargs.get('reservation_id')
        try:
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "La réservation demandée n'existe pas."},
                status=status.HTTP_404_NOT_FOUND
            )
        voiture_a_modifie = reservation.voiture
        if reservation.dateReservation <= timezone.now().date()  <= reservation.dateRetour:
            voiture_a_modifie.statutVoiture = True
        else:
             voiture_a_modifie.statutVoiture = False
             reservation.statutReservation = True
        voiture_a_modifie.save()
        reservation.save()
        return Response({"message": "Réservation fini avec succès."}, status=status.HTTP_200_OK)
    
#Classe pour afficher les réservations du client
class ReservationsDuClientView(APIView):
    def get(self, request, client_id):
        reservations = Reservation.objects.filter(client=client_id)  
        serializer = ReservationResponseSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Classe pour afficher les réservations d'un propriétaire
class ReservationsDunProprietaire(APIView):
    def get(self, request, proprietaire_id):
        try:
            reservations = Reservation.objects.filter(voiture__proprietaire=proprietaire_id)
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Aucune réservation trouvée pour ce propriétaire."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationResponseSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)