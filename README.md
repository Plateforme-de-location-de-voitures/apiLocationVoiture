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

2. `/role/<int:role_id>`
- Méthode : GET
- Description : Renvoie les détails d'un rôle spécifique identifié par son ID.
- Utilisation : **Postman**
  ![Doc 4](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/c5a1bb2f-1756-4fb0-9776-fccf15bd3f6b)

3. `/register`
- Méthode : POST
- Description : Permet à un utilisateur de s'inscrire dans l'application.
- Utilisation : **Postman**
  ![Doc 5](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/c7f14d33-2624-4b73-a22e-c2b91a420169)

4. `/login`
- Méthode : POST
- Description : Permet à un utilisateur de se connecter à l'application.
- Utilisation : **Postman**
  ![Doc 6](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/8e09a78b-7607-46d2-b327-4d1ad93ad532)

5. `/user`
- Méthode : GET
- Description : Renvoie les détails de l'utilisateur actuellement connecté en fonction de **l'access token** recupéré lors du login.
- Utilisation : **Postman**
  ![Doc 7](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/eb722080-426e-4632-8f10-a51ed85b3241)

7. `/logout`
- Méthode : POST
- Description : Permet à l'utilisateur actuellement connecté de se déconnecter.
- Utilisation : **Postman**
  ![Doc 8](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/453522a4-64a5-46e7-9170-5480dce997b7)
