# Favicon

> v 0.0.1-dev

A simple app based on from [realfavicongenerator.net](https://realfavicongenerator.net) and it's [recommended best practcies](https://realfavicongenerator.net/faq) to serve favicon assets at the root of the site.

This app, essentially, takes a list of favicon asset names and automatically creates Django RedirectViews to serve all the assets at the root of the site and redirect the urls to the approprate path under `STATIC_URL`.

## Notes

- This app does not support `browserconfig.xml` at this time
- This app does not support `site.webmanifest` at this time

## How To Use: 5 Easy Steps!

### 1. Generate your favicon:

[Click Here to Go to Real Favicon Generator](https://realfavicongenerator.net)

**Tips:**
- Check the "generate html_code.html" at the end of the generator wizard.

### 2. Update Settings

Update Django conf (sometimes `base.py` or `settings.py`):

```python

# We must install the app to use it.

INSTALLED_APPS = (
    # ... other apps omitted
    "app.favicon",
)

# Update context_processors (order is not important).

TEMPLATES = [
    {
        # ... other settings omitted
        "OPTIONS": {
            "context_processors": (
                # ... other processors omitted
                "app.favicon.context_processors.favicon_settings",
            ),
        },
    }
]

# Setup app settings.
# Favicon uses a single settings namespace, FAVICON.

FAVICON = {
    # Useful for cache-busting your favicon, optional.
    "favicon_version": "abc1234",

    # This base path will be relative to your STATIC_URL,
    # as it and the asset name are run through staticfiles_storage.url
    # when generating redirect urls.
    # Default is: /, optional
    "favicon_asset_base_path": "/favicon/",

    # Your list of assets.
    # It should match the favicon asset file names from the generator.
    # Do not include any path information, for example:
    #
    # NOT OK:
    # "foo/bar/baz/favicon.ico"
    #
    # OK:
    # "favicon.ico"
    #
    # Valid assets are:
    # - image files (.png, .svg, .jpg)
    #
    # NOTE: This app doesn't (currently) do any sanitizing of image names,
    #       if you're not using the generator use URL safe file names.

    "favicon_assets": [
        # ...
    ]
}
```

### 3. Update urls.py

Update your `urls.py` to include favicon app urls

```python
urlpatterns = [
    # ... other patterns omitted
    url(r'^', include("app.favicon.urls", namespace="app_favicon")),
]
```

### 4. Update favicon_head.html

Override/update the `favicon/favicon_head.html` template with what the generator included in `html_code.html`.


### 5. Update site base layout

Finally, update your `base.html` (or whatever the base layout file is for your site) with an include for the `favicon_head.html` template file:

```html
<!doctype html>
<!-- Actual layout code omitted -->
<html>
    <head>
        <!-- All other <head> code omitted -->
        {% include "favicon/favicon_head.html" %}
    </head>
    <body></body>
</html>
```
