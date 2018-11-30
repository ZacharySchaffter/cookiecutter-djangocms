from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.ui"
    label = "app_ui"
    verbose_name = "UI"

    def ready(self):
        pass
