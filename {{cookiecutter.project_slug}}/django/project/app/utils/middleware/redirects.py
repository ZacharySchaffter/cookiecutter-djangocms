from urllib.parse import urlparse
from django.apps import apps
from django.conf import settings
from django.contrib.redirects.models import Redirect
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseGone, HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


class RedirectFallbackMiddleware(MiddlewareMixin):
    """
    Better RedirectFallbackMiddleware.

    * Ignore query params when matching routes
    * Forward query params with redirect

    Usage:
        ```
        # settings.py
        MIDDLEWARE = (
            ...
            "app.utils.middleware.redirects.RedirectFallbackMiddleware"
        )
        ```
    """

    response_gone_class = HttpResponseGone
    response_redirect_class = HttpResponsePermanentRedirect

    def __init__(self, get_response=None):
        if not apps.is_installed('django.contrib.sites'):
            raise ImproperlyConfigured(
                "You cannot use RedirectFallbackMiddleware when "
                "django.contrib.sites is not installed."
            )
        super().__init__(get_response)

    def process_response(self, request, response):
        # No need to check for a redirect for non-404 responses.
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        current_site = get_current_site(request)
        parsed = urlparse(full_path)
        path = parsed.path
        query = parsed.query

        r = None

        try:
            r = Redirect.objects.get(site=current_site, old_path=path)
        except Redirect.DoesNotExist:
            pass

        if r is None and settings.APPEND_SLASH and not path.endswith('/'):
            try:
                r = Redirect.objects.get(
                    site=current_site,
                    old_path=(path + "/"),
                )
            except Redirect.DoesNotExist:
                pass

        if r is not None:
            if r.new_path == '':
                return self.response_gone_class()

            new_path = r.new_path + ("?" + query if query else "")
            return self.response_redirect_class(new_path)

        # No redirect was found. Return the response.
        return response
