![Doc 1](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/3ff915ba-6968-4da5-b0cb-feec260caed8)# apiLocationVoiture
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

#### users
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

#### marque
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

#### modele
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
  ![Doc 13](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/99c12ae1-572b-49f2-8843-2350cdc35ba4)

16. `/api/modele/delete/<int:modele_id>`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer un modèle existant en spécifiant son identifiant (modele_id) dans l'URL.

#### voiture
17. `/api/voitures`
- Méthode : GET
- Description : Cet endpoint permet de récupérer la liste des voitures disponibles.
  ![Doc 15](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/b00fa280-499d-4d2b-bd44-878a98c8bf0a)

18. `/api/voiture/create`
- Méthode : POST
- Description : Cet endpoint permet de créer une nouvelle voiture en envoyant les informations nécessaires pour la nouvelle voiture.
  ![Doc 14](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/7ad446d0-9d99-48b5-8ba0-2150633d1aaa)

19. `/api/voiture/<int:pk>`
- Méthode : GET
- Description : Cet endpoint permet de récupérer les détails d'une voiture spécifique en utilisant sa clé primaire (pk) dans l'URL. La clé primaire est généralement un identifiant unique qui permet d'identifier de manière univoque une voiture dans la base de données.

20. `/api/voiture/update/<int:pk>`
- Méthode : PUT
- Description : Cet endpoint permet de mettre à jour une voiture existante en spécifiant sa clé primaire (pk) dans l'URL et en envoyant les nouvelles informations de la voiture.

21. `/api/voiture/delete/<int:pk>`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer une voiture existante en spécifiant sa clé primaire (pk) dans l'URL.

#### imageVoiture
22. `/api/images/voitures`
- Méthode : GET
- Description : Cet endpoint permet de récupérer la liste des images de voitures disponibles (peut-être la liste de toutes les images de voitures dans la base de données).
  ![Doc 18](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/a2b9c935-e22d-4f79-9ff1-93a74e3b59ef)

23. `/api/images/voiture/<int:voiture_id>`
- Méthode : GET
- Description : Cet endpoint permet de récupérer les images associées à une voiture spécifique en utilisant son identifiant (voiture_id) dans l'URL.
  ![Doc 19](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/59e68201-b737-4350-b005-16ffe499c890)


24. `/api/image/voiture/create`
- Méthode : POST
- Description : Cet endpoint permet de créer une nouvelle image de voiture en envoyant les informations nécessaires pour la nouvelle image.
  ![Doc 16](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/00685903-f884-44dc-b12b-161bf90561b9)

  ![Doc 17](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/5ad225df-4e52-4535-9f66-0339194dcfd2)

25. `/api/image/voiture/<int:pk>`
- Méthode : GET
- Description : Cet endpoint permet de récupérer les détails d'une image de voiture spécifique en utilisant sa clé primaire (pk) dans l'URL.

26. `/api/image/voiture/delete/<int:pk>`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer une image de voiture existante en spécifiant sa clé primaire (pk) dans l'URL.

#### reservations
27. `/api/reservations`
- Méthode : GET
- Description : Cet endpoint permet de récupérer la liste des réservations disponibles.
  ![Doc 21](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/647e9d25-10b4-42b1-a08d-9315e9dc5041)

28. `/api/reservation/create`
- Méthode : POST
- Description : Cet endpoint permet de créer une nouvelle réservation en envoyant les informations nécessaires pour la nouvelle réservation.
  ![Doc 20](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/9ac3da81-e026-438e-b6bd-4db5c8267728)

29. `/api/reservation/recherche/<str:nom_client>`
- Méthode : GET
- Description : Cet endpoint permet de rechercher des réservations en fonction du nom du client (nom_client) fourni dans l'URL.

30. `/api/reservation/update/<int:reservation_id>/`
- Méthode : PUT
- Description : Cet endpoint permet de mettre à jour une réservation existante en spécifiant son identifiant (reservation_id) dans l'URL et en envoyant les nouvelles informations de la réservation.

31. `/api/reservation/delete/<int:reservation_id>/`
- Méthode : DELETE
- Description : Cet endpoint permet de supprimer une réservation existante en spécifiant son identifiant (reservation_id) dans l'URL.

32. `/api/reservation/detail/<int:reservation_id>/`
- Méthode : GET
- Description : Cet endpoint permet de récupérer les détails d'une réservation spécifique en utilisant son identifiant (reservation_id) dans l'URL.
  ![Doc 1](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/a9c6d485-01f9-4f4f-b016-a16d0c48be88)

33. `/api/fin/<int:reservation_id>/`
- Méthode : POST
- Description : Cet endpoint permet de marquer la fin d'une réservation spécifique en utilisant son identifiant (reservation_id) dans l'URL.

34. `/api/voiture/disponible/<str:date_reservation>/<str:date_retour>/`
- Méthode : GET
- Description : Cet endpoint permet de rechercher les voitures disponibles entre deux dates spécifiées (date_reservation et date_retour) dans l'URL.
  ![Doc 2](https://github.com/Plateforme-de-location-de-voitures/apiLocationVoiture/assets/101883211/a8c059c8-de8c-4707-bf89-9e0d0b7ea96a)
