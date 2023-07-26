from django.db import models
from modele.models import Modele

from users.models import Proprietaire

# Create your models here.
class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)
    numeroSerie = models.CharField(max_length=100, unique=True)
    vinNumber = models.CharField(max_length=100, unique=True)
    couleur = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    anneeFabrication = models.PositiveIntegerField()
    puissance = models.FloatField()
    imagePrincipal = models.ImageField(upload_to="voiture_images", default="", null=True, blank=True)
    statutVoiture = models.BooleanField()

    def __str__(self):
        return str(self.numeroSerie)