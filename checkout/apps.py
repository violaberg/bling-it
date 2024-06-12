from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    AppConfig class for the checkout app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Executes code when the application is ready.
        """
        import checkout.signals  # noqa: F401
