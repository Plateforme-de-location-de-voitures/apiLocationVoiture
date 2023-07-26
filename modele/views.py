from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response  
from modele.models import Modele  
from modele.serializers import  ModeleSerializer  
# Create your views here.

#fonction pour lister tous les modeles
class ModeleListAPIView(APIView):
   
    def get(self, request):
        modeles = Modele.objects.all()  
        serializer = ModeleSerializer(modeles, many=True)
        
        return Response(serializer.data) 

#fonction pour créer un modele 
class ModeleCreateAPIView(APIView):
   
    def post(self, request):
        serializer = ModeleSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#fonction pour modifier un modèle
class ModeleUpdateAPIView(APIView):
   
    def put(self, request, modele_id):
        try:
            modele = Modele.objects.get(pk=modele_id)
        except Modele.DoesNotExist:
            return Response({"error": "Ce modele n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ModeleSerializer(modele, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#fonction pour supprimer un modele 
class ModeleDeleteAPIView(APIView):

     def delete(self, request, modele_id):
        try:   
            modele = Modele.objects.get(pk=modele_id)
        except Modele.DoesNotExist:
            return Response({"error": "Le modele spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        modele.delete()
        return Response({"success": "Le modele a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)


           