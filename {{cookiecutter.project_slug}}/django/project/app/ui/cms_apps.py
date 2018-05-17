import logging
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from . import apps


log = logging.getLogger(__name__)


@apphook_pool.register()
class UIAppHook(CMSApp):
    name = _("UI")
    app_name = apps.Config.label

    def get_urls(self, page=None, language=None, **kwargs):
        return ["app.ui.urls", ]
