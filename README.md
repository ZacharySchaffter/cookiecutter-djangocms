[Virtualenv]: https://virtualenv.pypa.io/en/stable/ "Virtualenv Docs"
[Virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/ "Virtualenvwrapper Docs"
[Pipenv]: https://docs.pipenv.org/ "Pipenv Docs"
[Brew]: https://brew.sh/
[Klak]: https://klak.readthedocs.io/en/latest/index.html
[Click]: http://click.pocoo.org/6/


# CookieCutter DjangoCMS

## Requirements

- Python > 3.6.x
- [Virtualenv]+[Virtualenvwrapper] or [Pipenv]
- [Brew] (OSX, only)

## Local Development

Using `virtualenv/virtualenvwrapper`:

```bash
mkvirtualenv django-cookiecutter
pip install -r requirements/dev.txt
```

Using `pipenv`:

```
pipenv install -r requirements/dev.txt
pipenv shell
```

## Local Testing

> [Klak] is a tiny wrapper around [Click] that enables a _simple-Makefile-like_ experience by automatically consuming a similar `Clickfile` in the current working directory.

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

