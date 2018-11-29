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
[Pyenv]: https://github.com/pyenv/pyenv "Pyenv Docs"
[NVM]: https://github.com/creationix/nvm "NVM Docs"

# {{ cookiecutter.project_name }}

## System Requirements

> __NOTE:__ See [MacOs Setup](./docs/macos_setup.md) to verify your macine meets all the setup prerequisites.

- MacOS
- [Docker]
- [Git]
- [Python] (3.6.x)
- [Pyenv]
- [Pipenv]
- [NVM]
- [Node & Npm]
- [Heroku]

## Contributing

See [Contributing Docs](./CONTRIBUTING.md).

{% if cookiecutter.use_heroku.lower() == "y" %}
## Hosted Environments

| Env | Desc. | App | Remote | Link |
| :--  | :-- | :-- | :-- | :-- |
| Prod | Live | {{cookiecutter.heroku_slug}}-prod | `prod` | [View Site](https://{{cookiecutter.heroku_slug}}-prod.herokuapp.com) |
{% else %}
> TODO: Write Hosted Environment Documentation
{% endif %}

## Setup

> Hint: Follow steps in "Terminal session 1" first.

Terminal session 1:
```bash
# Setup virtual environment
pyenv global 3.6.7
pipenv install -r requirements/dev.txt --python $(pyenv which python)
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
# NOTE: If you get a warning about an unsupported prefix,
#       add the --delete prefix option as instructed.
nvm use --lts
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


## Deploys

{% if cookiecutter.use_heroku.lower() == "y" %}
__Notes__:

* Deploys use Heroku and require the [Heroku CLI] & [Git].
* For more information see [docks/heroku.md](./docs/heroku.md).

{% else %}
> TODO: Write Deploy Documentation
{% endif %}

## Project Automation

```bash
# See all top-level commands
klak --help

# See all sub-level commands
klak <command> --help

# See sub-level command help
klak <command> <subcommand> --help
```

## Contribute

- [See CONTRIBUTING.md](./CONTRIBUTING.md)

## Documentation

- [Docs](./docs)
