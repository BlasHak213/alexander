from django.apps import AppConfig


class FanSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fan_site'

    def ready(self):
        from . import signals
