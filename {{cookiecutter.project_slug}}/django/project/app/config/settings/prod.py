"""Production settings and globals."""

from .base import *

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

ALLOWED_HOSTS += (".herokuapp.com",)

SECRET_KEY = env("SECRET_KEY")

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

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

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

# Utils
# =====================================

SLACK_USER_NAME = env("SLACK_USER_NAME", default="Logger:PROD")

# Storages
# =====================================

AWS_HEADERS = {
    "Cache-Control": "max-age=31536000",
}
