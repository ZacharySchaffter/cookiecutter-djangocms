# -------------------------------------
# DOCKERFILE (LOCAL)
# -------------------------------------
# Create a container appropriate for Django and Django-Geo

FROM python:3.6

# Update and install system dependencies
# Django-Geo Libs: binutils, libproj-dev, gdal-bin, libgeoip1, python-gdal
# Django-i18n Libs: gettext libgettextpo-dev
RUN apt-get update -y && apt-get install -y \
    apt-utils \
    {% if cookiecutter.use_geo.lower() == "y" %}binutils \
    libproj-dev \
    gdal-bin \
    libgeoip1 \
    python3-gdal \{% endif %}
    gettext \
    libgettextpo-dev
