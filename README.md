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
2. `/role/<int:role_id>`
- Méthode : GET
- Description : Renvoie les détails d'un rôle spécifique identifié par son ID.
- Utilisation : **Postman**
3. `/register`
- Méthode : POST
- Description : Permet à un utilisateur de s'inscrire dans l'application.
- Utilisation : **Postman**
4. `/login`
- Méthode : POST
- Description : Permet à un utilisateur de se connecter à l'application.
- Utilisation : **Postman**
5. `/user`
- Méthode : GET
- Description : Renvoie les détails de l'utilisateur actuellement connecté en fonction de **l'access token** recupéré lors du login.
- Utilisation : **Postman**
7. `/logout`
- Méthode : POST
- Description : Permet à l'utilisateur actuellement connecté de se déconnecter.