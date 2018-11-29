"""Development settings and globals."""

from .base import *

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

# Installed Apps
# =====================================

INSTALLED_APPS += (
    "debug_toolbar",
    "storages",
)

# Middleware
# =====================================

MIDDLEWARE += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

# Logging
# =====================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(name)s:%(lineno)s %(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s")
        },
        "simple": {
            "format": "%(levelname)s %(asctime)s %(message)s"
        },
    },
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },

    "loggers": {
        "": {
            "handlers": ["stream", ],
            "level": LOG_LEVEL,
        },
        "django.db": {
            "handlers": ["stream", ],
            "level": LOG_LEVEL,
        },
        "z.pool": {
            "handlers": ["stream", ],
            "level": LOG_LEVEL,
        },
        "django.server": {
            "handlers": ["stream", ],
            "level": "WARNING",
        },
        "django": {
            "handlers": ["stream", ],
            "level": LOG_LEVEL,
        },
        "app.convergys": {
            "handlers": ["stream", ],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------

# Django Debug Toolbar
# =====================================


def show_toolbar(request):
    return True


INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
