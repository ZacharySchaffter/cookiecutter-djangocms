import logging
from os import path
from django.utils.text import slugify
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url
from .settings import favicon_settings


log = logging.getLogger(__name__)


FAVICON_ASSETS = favicon_settings["favicon_assets"]
FAVICON_ASSET_BASE_PATH = favicon_settings["favicon_asset_base_path"]


def redirect_view_factory(asset_name, permanent=True):
    asset_path = f"{FAVICON_ASSET_BASE_PATH}{asset_name}"
    asset_url = staticfiles_storage.url(asset_path)
    return RedirectView.as_view(url=asset_url, permanent=permanent)


def url_factory(asset_name, redirect_view_func):
    url_path = f'^{asset_name}'
    url_name = slugify(path.basename(asset_name))

    return url(url_path, redirect_view_func, name=url_name)


urlpatterns = [
    url_factory(asset_name, redirect_view_factory(asset_name))
    for asset_name in FAVICON_ASSETS
]
