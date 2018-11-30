import logging
from cms.models.pluginmodel import CMSPlugin


log = logging.getLogger(__name__)


class PluginModel(CMSPlugin):
    """
    Base CMSPlugin class.

    Naming CMSPlugin Subclasses:

    DjangoCMS conventions between CMSPlugin and CMSPluginBase
    are non-standard and not intuitive.

    This class,
    and it's companion in .cms_plugins, attempt to correct this
    by providing passthrough extensions that provide
    more Django-Like naming conventions.

    Notes:
        - CMSPlugin doesn't subclass db.models.Model directly but does
          implement db.models.base.ModelBase (the metaclass for models)
          and provides "model-like" functionality (additionally, DCMS
          conventions dictate to place plugins in models.py);
          so this naming convention fits right in.

    Example:
    ```
    @plugin_pool.register_plugin
    class FooPlugin(PluginModel):
        pass
    ```

    See Also:
        - app.cms.cms_plugins.PluginAdmin

    """

    class Meta:
        abstract = True

