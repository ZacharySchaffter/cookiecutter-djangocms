import logging
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from app.cms.cms_plugins import PluginAdmin as PluginAdminBase
from . import models


log = logging.getLogger(__name__)


class PluginAdmin(PluginAdminBase):
    """
    Base plugin admin for this app.

    See:
        - app.cms.cms_plugins.PluginAdmin for useage
    """
    module = _("UI")
