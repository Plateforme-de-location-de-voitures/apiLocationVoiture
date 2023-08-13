from django.db import models

from users.models import Client
from voiture.models import Voiture

# Create your models here.
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    dateReservation = models.DateField()
    dateRetour = models.DateField()
    statutReservation = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    voiture = models.ForeignKey(Voiture, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.dateReservation