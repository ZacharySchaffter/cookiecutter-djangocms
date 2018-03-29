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

Terminal session 1:
```bash
# Setup virtual environment
pipenv install -r requirements/dev.txt
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

## Automate

```bash
# To see latest help message run
klak --help
klak <command> --help
klak <command> <subcommand> --help
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
| Int | More stable, QA | {{cookiecutter.heroku_slug}}-int | `int` | [View Site](https://{{cookiecutter.heroku_slug}}-int.herokuapp.com) |
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

# Create int
klak heroku create -r int
klak heroku configure -r int

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

# Add int
klak heroku add_remote -r int

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

# Deploy int
klak heroku deploy -r int

# Deploy prod
klak heroku deploy -r prod
```
{% else %}
> TODO: Write Deploy Documentation
{% endif %}

## Contribute

- [See CONTRIBUTING.md](./CONTRIBUTING.md)

## Documentation

- [Docs](./docs)
