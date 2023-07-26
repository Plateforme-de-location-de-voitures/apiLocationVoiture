from django.contrib import admin

# Register your models here.
from .models import Marque

@admin.register(Marque)

class Marque(admin.ModelAdmin):
    
    pass