from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response  
from marque.models import Marque  
from marque.serializers import  MarqueSerializer  

# Create your views here.
#fonction pour lister toutes les marques
class MarqueListAPIView(APIView):
   
    def get(self, request):
        marques = Marque.objects.all()  
        serializer = MarqueSerializer(marques, many=True)
        
        return Response(serializer.data) 

#fonction pour créer une marque 
class MarqueCreateAPIView(APIView):
   
    def post(self, request):
        serializer = MarqueSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#fonction pour modifier une marque
class MarqueUpdateAPIView(APIView):
   
    def put(self, request, marque_id):
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "Cette marque n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarqueSerializer(marque , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#fonction pour supprimer une marque 
class MarqueDeleteAPIView(APIView):

     def delete(self, request, marque_id):
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "La marque spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        marque.delete()
        return Response({"success": "La marque a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)


           