# Importation des modules nécessaires
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.models import Role, Personne
from users.serializers import ClientSerializer, PersonneResponseSerializer, PersonneSerializer, ProprietaireSerializer, RoleResponseSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

#Classe pour afficher les rôles ajoutés
class RoleListAPIView(APIView):
    
    def get(self, request):
        roles = Role.objects.all() 
        serializer = RoleResponseSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Classe pour afficher les détails d'un rôle
class RoleDetailAPIView(APIView):

    def get(self, request, role_id):
        role = Role.objects.get(pk=role_id)
        serializer = RoleResponseSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Classe pour enregistrer un utilisateur
class RegisterAPIView(APIView):

    def post(self, request):
        role_id = request.data.get('role', None)

        if not role_id:
            return Response({"error": "Veuillez spécifier le rôle de l'utilisateur."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return Response({"error": "Rôle invalide."}, status=status.HTTP_400_BAD_REQUEST)

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

        return Response({"error": "Rôle invalide. Veuillez spécifier un rôle valide (ROLE_CLIENT ou ROLE_PROPRIETAIRE)."}, status=status.HTTP_400_BAD_REQUEST)

#Classe pour connecter un utilisateur  
class LoginAPIView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise AuthenticationFailed('Veuillez fournir une adresse e-mail et un mot de passe.')

        user = Personne.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Aucun utilisateur trouvé avec cette adresse e-mail.')

        if not user.check_password(password):
            raise AuthenticationFailed('Mot de passe incorrect.')

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

#Classe pour recupérer les informations d'un utilisateur connecté
class GetUserAPIView(APIView):

    def get(self, request):
        token = request.COOKIES.get('access_token')

        if not token:
            raise AuthenticationFailed('Non authentifié!!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Session expirée. Veuillez vous reconnecter!')
        except (jwt.DecodeError, jwt.InvalidTokenError) as e:
            raise AuthenticationFailed('Jeton invalide : {}'.format(e))

        user = Personne.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('Utilisateur non trouvé!')

        serializer = PersonneResponseSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Classe pour déconnecter un utilisateur
class LogoutAPIView(APIView):
    
    def post(self, request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'success',
        }
        return response