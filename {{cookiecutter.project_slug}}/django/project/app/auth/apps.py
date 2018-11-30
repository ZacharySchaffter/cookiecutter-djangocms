from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.auth"
    label = "app_auth"
    verbose_name = "Users"

    def ready(self):
        pass
