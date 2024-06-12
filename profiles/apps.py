from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the Profiles app.

    This class defines configuration options for the Profiles app, \
    such as the default
    auto field and the app's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
