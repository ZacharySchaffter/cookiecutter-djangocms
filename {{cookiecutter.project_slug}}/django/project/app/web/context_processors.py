import logging


log = logging.getLogger(__name__)


def web_settings(request):
    from django.conf import settings

    return {
        "web_settings": {
            "debug": getattr(settings, "DEBUG", False),
            "gtm_code": getattr(settings, "GTM_CODE", ""),
            "google_api_key": getattr(settings, "GOOGLE_API_KEY", ""),
        }
    }
