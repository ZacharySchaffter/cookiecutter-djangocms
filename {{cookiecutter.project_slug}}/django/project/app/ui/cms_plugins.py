import logging
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


log = logging.getLogger(__name__)


class UIAppBasePluginAdmin(CMSPluginBase):
    """
    Base CMSPluginBase class.

    This is an optional base plugin admin useful for
    sharing common customizations.

    Naming CMSPluginBase Subclasses:

    The CMSPluginBase name is too easily confused with the backing
    model base class for plugins, CMSPlugin. Since CMSPluginBase
    is, in actuality, an extension of `django.admin.ModelAdmin`
    anyway, we can follow a naming convention that
    makes more sense:

    ```
    @plugin_pool.register_plugin
    class FooPluginAdmin(UIAppBasePluginAdmin):
        pass
    ```

    """

    module = _("UI")
    name = _("Unnamed Plugin")
