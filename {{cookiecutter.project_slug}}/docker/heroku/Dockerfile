# -------------------------------------
# DOCKERFILE
# -------------------------------------
# Notes:
#   * You must build {{cookiecutter.project_slug}}/web
#    before building this image!
#
# See:
#   * Dockerfile Best Practices: https://goo.gl/ZQh6da

FROM {{cookiecutter.project_slug}}/web

# Build Args
# =====================================
# These are passed via the --build-arg flag during `docker build`
ARG ASSET_VERSION

# ENV Setup
# =====================================

# Single line form is preferred for caching
ENV PYTHONPATH=/usr/app/project:/usr/app/project/vendor \
    DJANGO_SETTINGS_MODULE=app.config.settings.prod

# Working Dir Setup
# =====================================
# We're about to work with the local context alot,
# let's make paths a little easir

WORKDIR /usr/app

# Install Dependencies
# =====================================

# Avoiding ./requirements/local.txt so we don't invalidate the cache for
# a local only update to reqs.

COPY ./django/requirements/base.txt ./requirements/base.txt
COPY ./django/requirements/production.txt ./requirements/production.txt
COPY ./django/requirements.txt ./

RUN pip install -r ./requirements.txt

# NOTE: Mostly everything that follows will invalidate the cache

# Copy Local Files
# =====================================

COPY ./django/ ./

# Copy env.build to .env temporarily for collect static
# NOTE: This overwrites any .env that may have been added from COPY above
RUN [ -f ./.build/.env ] || echo "Could not find ./.build/.env"
COPY ./django/.build/.env .env

# Run Collect Static
# =====================================

RUN python manage.py collectstatic --no-input

# We can get rid of .env now
# but leave env.build to keep as a build receipt.
RUN rm /usr/app/.env

# Asset Version
# =====================================
# Permanently embed ASSET_VERSION into container
# Separate from other ENV to avoid
# early / unintentional cache invalidation

ENV ASSET_VERSION=$ASSET_VERSION

# User Setup
# =====================================
# Recommended, run the image as non-root

RUN groupadd -r heroku && useradd --no-log-init -r -g heroku heroku
USER heroku

# Start the App
# =====================================
# CMD is required to run on Heroku
# $PORT is set by Heroku

CMD gunicorn app.config.wsgi --bind 0.0.0.0:$PORT -w 2 -k gevent
