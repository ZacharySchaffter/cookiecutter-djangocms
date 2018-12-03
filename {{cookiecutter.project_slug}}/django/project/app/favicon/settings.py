"""
Favicon settings

In a Django settings.py:

FAVICON = {
    "favicon_version": "",
    "favicon_assets = [],
    "favicon_asset_base_path = "/",
}

FAVICON settings:

favicon_version (str)             A 'version' querystring value (useful for busting favicon cache), optional
favicon_assets (list)             A list of asset names, do not include path information
favicon_assets_base_path (str)    The base path for favicon assets, prepended to redirect paths
                                  (NOTE: This path is run through staticfiles_storage.url),
                                  default is /

"""

from django.conf import settings

__all__ = ("favicon_settings", )

FAVICON_DEFAULTS = {
    "favicon_version": "",
    "favicon_asset_base_path": "/",
    "favicon_assets": [],
}

FAVICON_USER_SETTINGS = getattr(settings, "FAVICON", {})

# Python 3.5+
favicon_settings = {**FAVICON_DEFAULTS, **FAVICON_USER_SETTINGS}

# NOTE: Construct querystring if favicon_version is set
if favicon_settings["favicon_version"]:
    favicon_version = favicon_settings["favicon_version"]
    favicon_settings["favicon_asset_query_string"] = f"?v={favicon_version}"
