"""Django app configuration for the brave_orders application."""

from django.apps import AppConfig


class BraveOrdersConfig(AppConfig):
    """Application configuration for the brave_orders Django app.

    This configuration class defines metadata and initialization behavior
    for the brave_orders application, including the application name and
    any app-specific settings.

    Attributes:
        name (str): The full Python path to the application, used by Django
            to identify this app in INSTALLED_APPS.
    """

    name = "brave_orders"
