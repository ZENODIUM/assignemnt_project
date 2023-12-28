# apps.py

from django.apps import AppConfig
from django.conf import settings
import firebase_admin
from firebase_admin import credentials

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminapp'

    def ready(self):
        # Initialize Firestore
        cred = credentials.Certificate({
            "type": settings.FIREBASE_CONFIG["type"],
            "project_id": settings.FIREBASE_CONFIG["project_id"],
            "private_key_id": settings.FIREBASE_CONFIG["private_key_id"],
            "private_key": settings.FIREBASE_CONFIG["private_key"],
            "client_email": settings.FIREBASE_CONFIG["client_email"],
            "client_id": settings.FIREBASE_CONFIG["client_id"],
            "auth_uri": settings.FIREBASE_CONFIG["auth_uri"],
            "token_uri": settings.FIREBASE_CONFIG["token_uri"],
            "auth_provider_x509_cert_url": settings.FIREBASE_CONFIG["auth_provider_x509_cert_url"],
            "client_x509_cert_url": settings.FIREBASE_CONFIG["client_x509_cert_url"],
            "universe_domain": settings.FIREBASE_CONFIG.get("universe_domain", None),
        })

        firebase_admin.initialize_app(cred)
