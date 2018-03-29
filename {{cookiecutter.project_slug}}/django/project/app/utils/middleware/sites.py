from django.contrib.sites.models import Site
from django.conf import settings
from cms.utils.apphook_reload import reload_urlconf


class CMSSiteMiddleware(object):
    """
    Better SiteMiddleware with support for DjangoCms.

    Usage:
        ```
        # settings.py

        MIDDLEWARE = (
            ...
            "app.utils.middleware.sites.CMSSiteMiddleware",
        )

        DEFAULT_SITE = SITE_ID = 1
        ```

    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.DEFAULT_SITE_ID)

        request.current_site = current_site
        settings.SITE_ID = current_site.id

        # Added this to fix resolution errors in cms app/appconfigs
        # TODO: (revisit) Unsure about the overhead of running this
        #       on every request. So far though, I have not
        #       discovered any other workaround.
        reload_urlconf()

        response = self.get_response(request)

        return response
