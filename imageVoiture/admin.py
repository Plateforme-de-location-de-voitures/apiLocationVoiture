from django.contrib import admin

# Importer le modèle ImageVoiture depuis le fichier models.py
from .models import ImageVoiture

# Utiliser le décorateur @admin.register pour enregistrer le modèle ImageVoiture dans l'interface d'administration
@admin.register(ImageVoiture)
# Créer une classe ImageVoitureAdmin qui hérite de admin.ModelAdmin
class ImageVoitureAdmin(admin.ModelAdmin):
    # Ici, nous n'avons pas ajouté de configurations spécifiques pour l'interface d'administration.
    # La classe passe simplement avec le mot-clé "pass", ce qui signifie qu'elle utilise les valeurs par défaut pour l'affichage et le comportement.
    pass


# il faut créer un compte administrateur django puis allez dans l'interface admin de django pour testé l'ajout de l'image en fonction d'une voiture 
# l'interface django rest ne peut pas géré ça c'est pourquoi je l'ai fait dans la partie admin de django