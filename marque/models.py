from django.db import models

# Create your models here.
class Marque(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.nom