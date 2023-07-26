from django.db import models
from voiture.models import Voiture

# Create your models here.
class ImageVoiture(models.Model):
    id = models.AutoField(primary_key=True)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name='images')
    #ce champ image crée le sous fichier voiture_images dans lequel sera les images
    image = models.ImageField(upload_to="voiture_images", default="", null=True, blank=True)

    def __str__(self):
        return str(self.image)
