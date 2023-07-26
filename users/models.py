from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    libelle = models.CharField(max_length=225)

    def __str__(self):
        return self.code
    
class Personne(AbstractUser):
        
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    username = None
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=225)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Proprietaire(Personne):
    pass


class Client(Personne):
    pass