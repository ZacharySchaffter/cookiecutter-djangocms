# Heroku Post Deploy

## Purpose

The purpose of this document is to provide "post-deploy" best practices after deploying the site for the _first time_ to Heroku.


## Create a Home Page (Required)

> NOTE: Only applies to DjangoCMS

1. Open the __Django CMS > Pages__ app in /admin
2. Click "New Page"
3. Enter the following:
    - __Title__: Enter `Home`
4. Click Save

## Update Admin Credentials (Required)

1. Open the __Users > Users __ app in /admin
2. Find the "Admin" user (it's probably the only user in there)
3. Follow the process to set the user's credentials to a [strong password](http://bit.ly/google-strong-passwords).

## Disable Search Indexing (Required)

1. Open the __Robots > Rules__ app in /admin
2. Click "Add Rule"
3. Enter the following:
    - __Robot__: `*`
    - __Available Sites__: Click "Choose All"
    - __Disallowed__: Click the `+` sign and enter: `/` and click save. When you return to the main screen select "Choose All".
4. Click Save

## Update Sites (Recommended)

1. Open the __Sites > Sites__ app in /admin
2. Click on the desired record (typically there is only a single record)
3. Enter the following:
    - __Domain__: Enter the full Heroku app domain (without the protocol/sheme). For example, __my-app.herokuapp.com__.
    - __Name__: Enter a human-readable name.
4. Click Save
