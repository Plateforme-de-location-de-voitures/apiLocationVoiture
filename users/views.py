# Importation des modules nécessaires
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.models import Role, Personne
from users.serializers import ClientSerializer, PersonneResponseSerializer, PersonneSerializer, ProprietaireSerializer, RoleResponseSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

#Fonction pour afficher les rôles
class RoleListAPIView(APIView):

    def get(self, request):
        roles = Role.objects.all() 
        serializer = RoleResponseSerializer(roles, many=True)
        return Response(serializer.data)

#Fonction pour afficher les détails d'un rôle
class RoleDetailAPIView(APIView):
    
    def get(self, request, pk):
        role = Role.objects.get(pk=pk)
        serializer = RoleResponseSerializer(role)
        return Response(serializer.data)

#Fonction pour enregistrer un utilisateur
class RegisterAPIView(APIView):

    def post(self, request):
        role_id = request.data.get('role', None)

        if not role_id:
            return Response({"error": "Role is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return Response({"error": "Invalid role."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if role.code == 'ROLE_CLIENT':
            client_serializer = ClientSerializer(data=request.data)
            client_serializer.is_valid(raise_exception=True)
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_201_CREATED)
        elif role.code == 'ROLE_PROPRIETAIRE':
            proprietaire_serializer = ProprietaireSerializer(data=request.data)
            proprietaire_serializer.is_valid(raise_exception=True)
            proprietaire_serializer.save()
            return Response(proprietaire_serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": "Invalid role."}, status=status.HTTP_400_BAD_REQUEST)

#Fonction pour connecter un utilisateur  
class LoginAPIView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Personne.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()

        response.set_cookie(key='access_token', value=token, httponly=True)
        response.data = {
            'access_token': token
        }
        return response

#Fonction pour recupérer les informations d'un utilisateur connecté
class GetUserAPIView(APIView):

    def get(self, request):
        token = request.COOKIES.get('access_token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except (jwt.DecodeError, jwt.InvalidTokenError) as e:
            raise AuthenticationFailed('Invalid token: {}'.format(e))

        user = Personne.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('User not found!')

        serializer = PersonneResponseSerializer(user)
        return Response(serializer.data)

#Fonction pour déconnecter un utilisateur
class LogoutAPIView(APIView):
    
    def post(self, request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'success'
        }
        return response