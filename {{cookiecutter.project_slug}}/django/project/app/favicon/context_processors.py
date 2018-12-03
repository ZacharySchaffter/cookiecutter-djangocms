def favicon_settings(request):
    from .settings import favicon_settings

    return {
        "favicon_settings": favicon_settings
    }
