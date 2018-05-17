[Docker for Mac]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Docker]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Docker Hub]: https://hub.docker.com/ "Docker Hub Homepage"
[Node & Npm]: https://nodejs.org/en/download/ "Intsall Node"
[Homebrew]: http://brew.sh/ "Homebrew Homepage"
[Heroku]: https://www.heroku.com/ "Heroku Homepage"
[Virtualenv]: https://virtualenv.pypa.io/en/stable/ "Virtualenv Docs"
[Virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/ "Virtualenvwrapper Docs"
[Pipenv]: https://docs.pipenv.org/ "Pipenv Docs"
[Heroku CLI]: https://devcenter.heroku.com/articles/heroku-cli "Heroku CLI Homepage"
[Git]: https://example.com "Git Homepage"
[Python]: https://example.com "Python Homepage"

# {{ cookiecutter.project_name }}

## System Requirements

- macOS
- [Homebrew]
- [Git]
- [Python] (3.6)
- [Pipenv]
- [Docker]
- [Node & Npm]

## Setup

Follow the instructions in [Python Setup](./docs/python_setup.md) if you've never setup your machine for virtualized, local Python/Django development.

> Hint: Follow steps in "Terminal session 1" first.

Terminal session 1:
```bash
# Setup virtual environment
pipenv install
pipenv shell

# Start local dev
# -b builds the local {{cookiecutter.project_slug}}/web docker image
klak up -b
klak init
klak serve
```

Terminal session 2:
```bash
# Activate virtual env (if not already activated)
pipenv shell

# Compile/watch static assets
klak watch
```

{% if cookiecutter.use_heroku.lower() == "y" %}
Terminal session 3:
1. Follow: [Heroku:Add Remotes](#add-remotes)
2. Follow: [Heroku:Download/Import Remote Data](#download-import-remote-data)
{% endif %}

> [View Site](http://localhost:8000)

## Start

__STOP:__ You must first complete [Setup](#setup)!

Terminal session 1:

```bash
# Activate virtual env (if not already activated)
pipenv shell

# Start local dev
klak up
klak serve
```

Terminal session 2:

```bash
# Activate virtual env (if not already activated)
pipenv shell

# Compile/watch assets
klak watch
```

> [View Site](http://localhost:8000)

## Test

```bash
# Activate virtual env
pipenv shell

# Run Python / Django test suite
klak test
```

## Deploys

{% if cookiecutter.use_heroku.lower() == "y" %}
__Notes__:

* Deploys use Heroku and require the [Heroku CLI] & [Git].
* For more information see [docks/heroku.md](./docs/heroku.md).

### Environments

| Env | Desc. | App | Remote | Link |
| :--  | :-- | :-- | :-- | :-- |
| Dev | Least stable | {{cookiecutter.heroku_slug}}-dev | `dev` | [View Site](https://{{cookiecutter.heroku_slug}}-dev.herokuapp.com)  |
| QA | More stable, QA | {{cookiecutter.heroku_slug}}-qa | `qa` | [View Site](https://{{cookiecutter.heroku_slug}}-qa.herokuapp.com) |
| Prod | Live | {{cookiecutter.heroku_slug}}-prod | `prod` | [View Site](https://{{cookiecutter.heroku_slug}}-prod.herokuapp.com) |

### Create Apps

__Notes__:

* If the apps already exist, instead follow [Add Remotes](#add-remotes).

```bash
# Activate virtual env (if not already activated)
pipenv shell

# Usually only necessary once per system
klak heroku init
# __OR__ (if you've run the above before)
klak heroku login

# Create dev
klak heroku create -r dev
klak heroku configure -r dev

# Create qa
klak heroku create -r qa
klak heroku configure -r qa

# Create prod
klak heroku create -r prod
klak heroku configure -r prod
```

### Add Remotes

__Notes__:

* If you haven't added apps yet, instead follow [Create Apps](#create-apps).

```bash
# Add dev
klak heroku add_remote -r dev

# Add qa
klak heroku add_remote -r qa

# Add prod
klak heroku add_remote -r prod
```

### Deploy Latest

__Notes__:

* If you haven't added apps yet first see [Create Apps](#create-apps).
* If the apps already exist, first see [Add Remotes](#add-remotes).

```bash
# Deploy dev
klak heroku deploy -r dev

# Deploy qa
klak heroku deploy -r qa

# Deploy prod
klak heroku deploy -r prod
```

### Download/Import Remote Data

* Requires that you've followed [Setup](#setup)
* Requires that you've followed either [Create Apps](#create-apps) or [Add Remotes](#add-remotes)

```bash
# NOTE:
#   * Stop any running development server process before continuing...
#   * Add an option of --capture to get the latest data;
#    for example: klak heroku import_db --capture -r dev

# Import dev db
klak heroku import_db -r dev

# Import qa db
klak heroku import_db -r qa

# Import prod db
klak heroku import_db -r prod
{% else %}
> TODO: Write Deploy Documentation
{% endif %}

## Automation

```bash
# To see latest help message run
klak --help
klak <command> --help
klak <command> <subcommand> --help
```

## Contribute

- [See CONTRIBUTING.md](./CONTRIBUTING.md)

## Documentation

- [Docs](./docs)
