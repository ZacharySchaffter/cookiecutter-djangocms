import base64
from django.http import HttpResponse
from django.middleware.common import CommonMiddleware
from django.conf import settings


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

        authtype, auth = HTTP_AUTHORIZATION.split(" ")
        auth = base64.b64decode(auth)
        username, password = auth.split(b":")
        username = username.decode("utf-8")
        password = password.decode("utf-8")

        if username == BASIC_AUTH_USER and password == BASIC_AUTH_PASS:
            return

        response = HttpResponse("Auth Required", status=401)
        response["WWW-Authenticate"] = 'Basic realm = "bat"'
        return response
