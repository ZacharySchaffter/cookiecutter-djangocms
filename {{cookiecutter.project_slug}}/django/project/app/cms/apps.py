from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.cms"
    label = "app_cms"
    verbose_name = "CMS Extensions"

    def ready(self):
        pass
