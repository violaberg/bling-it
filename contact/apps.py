from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Configuration class for the contact app.

    This class defines the configuration for the contact app. It specifies
    the default auto field to be used for model auto-increment primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
