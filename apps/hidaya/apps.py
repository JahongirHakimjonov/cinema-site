from django.apps import AppConfig


class HidayaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.hidaya"

    def ready(self):
        import apps.hidaya.signals  # noqa
