import base64
from urllib.parse import urlparse
from django.http import HttpResponse
from django.middleware.common import CommonMiddleware
from django.conf import settings
from django.apps import apps
from django.contrib.redirects.models import Redirect
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseGone, HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


class BasicAuthMiddleware(CommonMiddleware):
    """
    Create a "BasicAuth" like experience using Django middleware.

    Usage:
        ```
        # settings.py

        MIDDLEWARE = (
            ...
            "app.utils.middleware.basicAuth.BasicAuthMiddleware",
        )

        BASIC_AUTH = True
        BASIC_AUTH_USER = "user"
        BASIC_AUTH_PASS = "password"
        ```

    """

    def process_request(self, request):
        BASIC_AUTH = getattr(settings, "BASIC_AUTH", False)
        BASIC_AUTH_USER = getattr(settings, "BASIC_AUTH_USER", None)
        BASIC_AUTH_PASS = getattr(settings, "BASIC_AUTH_PASS", None)
        HTTP_AUTHORIZATION = request.META.get("HTTP_AUTHORIZATION", False)

        if not BASIC_AUTH or not HTTP_AUTHORIZATION:
            return

        _, auth = HTTP_AUTHORIZATION.split(" ")
        auth = base64.b64decode(auth)
        username, password = auth.split(b":")
        username = username.decode("utf-8")
        password = password.decode("utf-8")

        if username == BASIC_AUTH_USER and password == BASIC_AUTH_PASS:
            return

        response = HttpResponse("Auth Required", status=401)
        response["WWW-Authenticate"] = 'Basic realm = "bat"'
        return response


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
