from django.apps import AppConfig
import logging


log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.favicon"
    label = "app_favicon"
    verbose_name = "Favicon"

    def ready(self):
        pass
