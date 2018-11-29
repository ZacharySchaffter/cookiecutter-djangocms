# Pre-Launch Checklist

## Purpose

The purpose of this document is to describe a set of Django best-practices before a site launches.

## General

### General: Accounts

- [ ] Verify all 3rd-party accounts are attached to client owned emails
- [ ] Verify all 3rd-party account passwords are known-to / managed by the client
- [ ] Verify all 3rd-party subscriptions are set up and active

### General: Analytics

- [ ] Ensure either GTM or GA is configured and working (if applicable)
- [ ] Ensure any other expected tracking is configured and working

### General: DNS

- [ ] Reduce TTL 24-hours before launch (if applicable)

### General: Security

- [ ] SSL cert is valid and enabled

### General: SEO

- [ ] Ensure all pages have unique meta/page titles
- [ ] Ensure page titles are correctly formatted to [SEO best practices](https://moz.com/learn/seo/title-tag)
- [ ] Ensure home page has unique meta description
- [ ] Ensure all other pages have unique meta descriptions (optional and only recommended if descriptions are unique; otherwise only set home page description)
- [ ] Ensure the Robots app in Django admin is set to allow crawling
- [ ] Ensure [Django Sitemaps](http://bit.ly/django-sitemaps) are enabled (if applicable)
- [ ] Ensure all 301 redirects are in place and functioning

### General: Site Performance

- [ ] Test site using tools at [Pingdom](https://tools.pingdom.com/)
- [ ] Ensure all static assets are delivered using `gzip` and minified.
- [ ] Ensure all site images are optimized (including CMS content!)
- [ ] Ensure app monitoring is in place and functioning (if applicable)

## Django

- [ ] Remove test accounts
- [ ] Ensure Admin account uses a [strong password](http://bit.ly/google-strong-passwords)

### Django: Settings

- [ ] Review & verify that settings files contain __no private information or credentials__
- [ ] Review & verify user configurable settings pull from environment
- [ ] Review & verify in all files (base.py, local.py, prod.py):
    - `ALLOWED_HOSTS`: include appropriate production domains and sub-domains
    - `django.middleware.clickjacking.XFrameOptionsMiddleware`: is enabled in `MIDDLEWARE`
- [ ] Review & verify in production settings (prod.py):
    - `DEBUG`: is set to `False`
    - `SECRET_KEY`: is set to a unique value
    - `SECURE_PROXY_SSL_HEADER`: is set to `('HTTP_X_FORWARDED_PROTO', 'https')`
    - `SECURE_SSL_REDIRECT`: is set to `True`
    - `SESSION_COOKIE_SECURE`: is set to `True`
    - `CRSF_COOKIE_SECURE`: is set to `True`

## Django CMS

- [ ] Verify all pages are published
- [ ] Verify all page in menu visibility is set appropriately
- [ ] Verify all page permissions are set appropriately
- [ ] Verify all page order is set appropriately

### Django CMS: Settings

- [ ] Review and verify in production settings (prod.py):
    - `CMS_PLUGIN_CACHE`: is set to `True`
    - `CMS_PLACEHOLDER_CACHE`: is set to `True`
    - `CMS_PAGE_CACHE` is set to `True`


## Heroku

### Heroku: Config

- [ ] Verify all required config is present and set appropriately
- [ ] Review the following settings:
    - `LOG_LEVEL`: is set to `ERROR`
    - `GA_CODE`: is set appropriately
    - `UPLOADCARE_PUB_KEY`: is set to the production value
    - `UPLOADCARE_SECRET_KEY`: is set to the production value
    - All security settings are set to production values (see: [Django: Settings](#django-settings))

### Heroku: Resources

- [ ] Verify Heroku Dynos are upgraded from Hobby (Standard 2x, normally)
- [ ] Verify Postgres is upgraded (Standard 0, normally)
- [ ] Verify all other resources are upgraded (if applicable)
- [ ] Increase the default gevent workers in [Dockerfile](./Dockerfile) `CMD` to something like: `CMD gunicorn app.config.wsgi --bind 0.0.0.0:$PORT -w 5 -k gevent` <sup>[1](#footnote-1)</sup><sup>[2](#footnote-2)</sup>



# Post-Launch Checklist

## General

### General: DNS

- [ ] Raise DNS TTL to previous value (if applicable)

### General: SEO

- [ ] Submit sitemaps via [Google Search Console](https://search.google.com/search-console/about) (must use client owned account)

---
<sup id="footnote-1">1</sup> This example works well for Standard 2x, see: [Heroku – Python/Gunicorn Docs](http://bit.ly/heroku-gunicorn) for more information.

<sup id="footnote-2">2</sup> You may need to configure workers dynamically if running more than one Heroku environment.

