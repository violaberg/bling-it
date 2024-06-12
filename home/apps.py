from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the Home app.

    This class defines the configuration for the Home app, \
    including the default auto field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
