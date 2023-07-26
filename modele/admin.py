from django.contrib import admin

# Register your models here.
from .models import Modele

@admin.register(Modele)

class Modele(admin.ModelAdmin):
   
    pass