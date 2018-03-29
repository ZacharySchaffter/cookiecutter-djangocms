[Heroku CLI]: https://devcenter.heroku.com/articles/heroku-cli "Heroku CLI Homepage"
[Heroku Container Registry & Runtime]: https://devcenter.heroku.com/articles/container-registry-and-runtime

# Heroku

## Required

- Requirements from [README.md](../README.md)
- A Heroku Account & the [Heroku CLI]

## Docs

- [Heroku Dev Center](https://devcenter.heroku.com/)
- [Heroku Container Registry & Runtime]

## Preamble

This boilerplate can:

* Initialize your machine for Heroku/Heroku Docker (OSX only)
* Create Heroku app(s)
* Configure Heroku app(s)
* Deploy Heroku app(s)

## Setup Heroku

```bash
# Follow the prompts (OSX Only)
klak heroku init
```

## Create App(s)

__Notes__:

* Only create app(s) if they _do not already exist_.
* If the apps already exist, see [Add Existing App(s)](#add-existing-apps) instead.

```bash
# Takes a (optional) positional <HEROKU_SLUG> arg (default: {{cookiecutter.heroku_slug}})
# Takes a required option --heroku_remote | -r
klak heroku create -r dev

# Also:
# Takes a (optional) positional <HEROKU_SLUG> arg (default: {{cookiecutter.heroku_slug}})
# Takes a required option --heroku_remote | -r
klak heroku configure -r dev
```

## Add Existing App(s)

```bash
# Takes a (optional) positional <HEROKU_SLUG> arg (default: {{cookiecutter.heroku_slug}})
# Takes a required option --heroku_remote | -r
klak heroku add_remote -r dev
```

## Deploy

__Notes__:

* If you haven't added apps yet first see [Create Apps](#create-apps).
* If the apps already exist, first see [Add Remotes](#add-remotes).

```bash
# Takes a (optional) positional <HEROKU_SLUG> arg (default: {{cookiecutter.heroku_slug}})
# Takes a required option --heroku_remote | -r
klak heorku deploy -r dev

# Optional: Open app in browser
heroku open -r dev
```

## Troubleshooting

To see Heroku help:

```bash
heroku help
heroku help TOPIC
heroku help TOPIC:COMMAND
```

To see Heroku app logs:

```bash
heroku logs [-r, --remote <REMOTE_NAME>] [--tail]
```

To see app info:

```bash
heroku info [-r, --remote <REMOTE_NAME>]
```

To see app config:

```bash
heroku config [-r, --remote <REMOTE_NAME>]
```

To open app in browser:

```bash
heroku open [-r, --remote <REMOTE_NAME>]
```

## Appendix: Multiple Heroku Remotes

### Managing multiple remotes

When a local repo points to more than one Heroku app it can get confusing which application Heroku commands will run against.

If we want to run a command on a specific remote (app), we can pass the `-r` or `--remote` flag:

```bash
# For example:
heroku config:set SOME_VAR=<some-value> --remote <heroku-remote-name>
```

### Set a default remote

Typing `-r <remote-name>` can be a bit tiring, so we can configure Git to point Heroku to a default remote.

```bash
# Optional:
# Manually set heroku.remote in git config
# This eliminates the need to specify -r constantly
git config heroku.remote <heroku-remote-name>
```

>  See [Heroku Multiple Environments](https://devcenter.heroku.com/articles/multiple-environments) for more info.
