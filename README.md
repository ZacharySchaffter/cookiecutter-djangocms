[Pipenv]: https://docs.pipenv.org/ "Pipenv Docs"
[Pyenv]: https://github.com/pyenv/pyenv "Pyenv Docs"
[Klak]: https://klak.readthedocs.io/en/latest/index.html
[Click]: http://click.pocoo.org/6/


# CookieCutter DjangoCMS

## Requirements

- Python (3.6.x)
- [Pipenv]
- [PyEnv]

## Local Development


Using `pipenv`:

```bash
# NOTE: If using pyenv, --python $(pyenv which python)
# NOTE: If using something other than pyenv --python $(which python)

pipenv install -r requirements/dev.txt --python /path/to/python
pipenv shell
```

## Local Testing

> NOTE: [Klak] is a tiny wrapper around [Click] that enables a _Makefile-like_ experience.

__See available commands:__

```bash
klak --help
```

__"Bake" a local copy of this template:__

```bash
# It's recommended to direct this command at a dir
# that is _not_ this project's dir.
klak cookiecutter bake -o /path/to/bake/dir

# Follow prompts.

# In another session (recommended)
cd /path/to/bake/dir

# Follow the template's README for local development.
```

__Run Python test suite:__

```bash
klak test py
```

## Links

- [CookieCutter](https://github.com/audreyr/cookiecutter)
- [Klak]
- [Click]

