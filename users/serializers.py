from rest_framework import serializers
from users.models import Client, Personne, Proprietaire, Role

class RoleResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','nom','prenom','email','password','telephone','role')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PersonneSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Personne

class ClientSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Client

class ProprietaireSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Proprietaire

class PersonneResponseSerializer(serializers.ModelSerializer):
    role = RoleResponseSerializer()
    class Meta:
        model = Personne
        fields = ('id','nom','prenom','email','password','telephone','role')
        extra_kwargs = {
            'password': {'write_only': True}
        }
