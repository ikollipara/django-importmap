from django.apps import AppConfig


class DjangoImportmapsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_importmaps"

    def ready(self) -> None:
        from importlib import import_module

        from django.conf import settings
        from django.core.exceptions import ImproperlyConfigured

        try:
            import_module(getattr(settings, "IMPORTMAP", "importmap"))
        except Exception:
            raise ImproperlyConfigured("IMPORTMAP must be a python module path")
