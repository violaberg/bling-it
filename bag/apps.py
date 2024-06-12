from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' Django app.

    Attributes:
        default_auto_field (str): The name of the field \
        to use for automatic primary key generation.
        name (str): The name of the Django app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
