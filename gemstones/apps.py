from django.apps import AppConfig


class GemstonesConfig(AppConfig):
    """
    AppConfig for the gemstones app.

    This class defines configuration settings for the gemstones app,
    such as the default auto field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gemstones'
