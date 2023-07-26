# apiLocationVoiture
API implémentée en Django Rest Framework qui nous permettra de gérer les compagnies de réservation de voiture.

### Installation des packages de requirements.txt

```shell
pip install -r requirements.txt
```

### Configuration de la base de données
Le SGBD (Système de Gestion de Base de Données) utilisé dans ce projet est MySQL. Assurez-vous que vous avez installé MySQL sur votre machine et configuré les informations d'accès (nom d'utilisateur, mot de passe, hôte, etc.) dans le fichier `settings.py` de l'application Django.

Dans le fichier `settings.py` (situé dans le dossier du projet), vous trouverez une section appelée `DATABASES`, qui ressemblera à ceci :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nom_de_votre_base_de_donnees',
        'USER': 'votre_nom_d_utilisateur_mysql',
        'PASSWORD': 'votre_mot_de_passe_mysql',
        'HOST': 'localhost',  # Ou l'adresse IP de votre serveur MySQL
        'PORT': '3306',  # Port MySQL par défaut
    }
}
```

### Migrations des tables dans la base de données
```shell
python manage.py migrate
```

### Démarrage du serveur
```shell
python manage.py runserver
```

### Endpoints disponibles

1. `/api/roles`
- Méthode : GET
- Description : Renvoie la liste des rôles disponibles dans l'application.
- Utilisation : Pour tester cette route, vous devez enregistrer le rôle à partir de l'espace admin de **PhpMyAdmin** avant de recupérer la liste des rôles enregistrés.
  ![Doc 1](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/1387b872-6b37-4f6d-b5f6-00fd640e4d25)
  
  ![Doc 2](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/d38b2668-a457-418f-9ad9-cde216884f84)

  ![Doc 3](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/4fcab34d-2114-4402-89f2-2887e0550615)

2. `/api/role/<int:role_id>`
- Méthode : GET
- Description : Renvoie les détails d'un rôle spécifique identifié par son ID.
- Utilisation : **Postman**
  ![Doc 4](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/c5a1bb2f-1756-4fb0-9776-fccf15bd3f6b)

3. `/api/register`
- Méthode : POST
- Description : Permet à un utilisateur de s'inscrire dans l'application.
- Utilisation : **Postman**
  ![Doc 5](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/c7f14d33-2624-4b73-a22e-c2b91a420169)

4. `/api/login`
- Méthode : POST
- Description : Permet à un utilisateur de se connecter à l'application.
- Utilisation : **Postman**
  ![Doc 6](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/8e09a78b-7607-46d2-b327-4d1ad93ad532)

5. `/api/user`
- Méthode : GET
- Description : Renvoie les détails de l'utilisateur actuellement connecté en fonction de **l'access token** recupéré lors du login.
- Utilisation : **Postman**
  ![Doc 7](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/eb722080-426e-4632-8f10-a51ed85b3241)

7. `/api/logout`
- Méthode : POST
- Description : Permet à l'utilisateur actuellement connecté de se déconnecter.
- Utilisation : **Postman**
  ![Doc 8](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/453522a4-64a5-46e7-9170-5480dce997b7)

9. `/api/marques`
- Méthode : GET
- Description : Cet endpoint permet de récupérer la liste des marques disponibles.
  ![Doc 10](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/bd40d1af-3c82-47cc-bee8-07fc1dd829c4)

10. `/api/marque/create`
- Méthode : POST
- Description : Cet endpoint permet de créer une nouvelle marque en envoyant les informations nécessaires pour la nouvelle marque.
  ![Doc 9](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/25b2363a-d9c3-4cf9-9d5a-994320cd4b6e)

11. `/api/marque/update/<int:marque_id>`
- Méthode : PUT
- Description : Cet endpoint permet de mettre à jour une marque existante en spécifiant son identifiant (marque_id) dans l'URL et en envoyant les nouvelles informations de la marque.

12. `/api/marque/delete/<int:marque_id>`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer une marque existante en spécifiant son l'id de la marque

13. `/api/modeles`
- Méthode : GET
- Description : Cet endpoint permet de récupérer la liste des modèles (modeles) disponibles.
  ![Doc 12](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/8d408184-e080-46a7-8665-be3c75018801)

14. `/api/modele/create`
- Méthode : POST
- Description : Cet endpoint permet de créer un nouveau modèle en envoyant les informations nécessaires pour le nouveau modèle.
  ![Doc 11](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/c728b807-f3b5-46a8-93d5-9aedb4fe64aa)

15. `/api/modele/update/<int:modele_id>`
- Méthode : PUT
- Description : Cet endpoint permet de mettre à jour un modèle existant en spécifiant son identifiant (modele_id) dans l'URL et en envoyant les nouvelles informations du modèle.

16. `/api/modele/delete/<int:modele_id>`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer un modèle existant en spécifiant son identifiant (modele_id) dans l'URL.
