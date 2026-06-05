from django.apps import AppConfig


class ApppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals
