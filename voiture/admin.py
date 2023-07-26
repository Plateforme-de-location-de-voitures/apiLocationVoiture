from django.contrib import admin

# Register your models here.
from .models import Voiture

@admin.register(Voiture)

class Voiture(admin.ModelAdmin):
   
    pass