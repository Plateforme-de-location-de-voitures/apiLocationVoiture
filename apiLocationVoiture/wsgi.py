"""
WSGI config for apiLocationVoiture project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from scheduler import start_scheduler
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiLocationVoiture.settings')
#appeler le fichier scheduler
application = get_wsgi_application()

start_scheduler() 

