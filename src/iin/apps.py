from django.apps import AppConfig


class IinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iin'

    def ready(self):
        from . import lookups  # noqa: F401
