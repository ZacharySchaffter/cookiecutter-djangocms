from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.shared"
    label = "app_shared"
    verbose_name = "Shared"

    def ready(self):
        pass
