import logging
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


log = logging.getLogger(__name__)


class PluginAdmin(CMSPluginBase):
    """
    Base CMSPluginBase class.

    Naming CMSPluginBase Subclasses:

    DjangoCMS conventions between CMSPlugin and CMSPluginBase
    are non-standard and not intuitive.

    This class, and it's companion PluginModel,
    attempt to correct this by providing passthrough
    extensions that provide more Django-Like naming conventions.

    Notes:
        - CMSPluginBase is a subclass of admin.ModelAdmin
          so this naming convention of PluginAdmin fits right in.

    Example:
    ```
    @plugin_pool.register_plugin
    class FooPlugin(PluginModel):
        pass
    ```

    See Also:
        - app.cms.models.Plugin

    """

    module = _("Unnamed Module")
    name = _("Unnamed Plugin")
