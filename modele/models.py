from django.db import models
from marque.models import Marque

# Create your models here.
class Modele(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25, default='')
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
