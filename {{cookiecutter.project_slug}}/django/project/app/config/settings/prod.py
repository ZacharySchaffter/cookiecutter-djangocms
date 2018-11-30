"""Production settings and globals."""

from .base import *

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Installed Apps
# =====================================

INSTALLED_APPS += (
    "gunicorn",
    "storages",
)

# Databases
# =====================================

{% if cookiecutter.use_geo.lower() == "n" %}
DATABASES["default"]["ENGINE"] = "django_postgrespool"
{% endif %}

DATABASE_POOL_ARGS = {
    "max_overflow": 7,
    "pool_size": 7,
    "recycle": 300,
}

# Staticfiles
# =====================================

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

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

