[Docker for Mac]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Docker]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Node & Npm]: https://nodejs.org/en/download/ "Intsall Node"
[Homebrew]: http://brew.sh/ "Homebrew Homepage"
[Virtualenv]: https://virtualenv.pypa.io/en/stable/ "Virtualenv Docs"
[Virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/ "Virtualenvwrapper Docs"
[Pipenv]: https://docs.pipenv.org/ "Pipenv Docs"
[Git]: https://example.com "Git Homepage"
[Python]: https://example.com "Python Homepage"
[Iterm2]: https://iterm2.com/downloads.html "Iterm2 Downloads"


> _NOTE: This doc assumes a fairly novice level when configuring bash preferences on a computer with MacOS. If you've already customized __.bash_profile__ (especially `PATH` settings) and/or have one or more of the following installed, use your best judgement when following the steps of this document._

# Python Setup

This project requires a machine setup for Python and virtualized local Python/Django development.

## System Requirements

- MacOS
- XCode Commandline Tools
- Bash and a configured __.bash_profile__
- [Homebrew]
- [Git]
- [Python] (3.6)
- [Pipenv]
- [Docker]
- [Node & Npm]

## 1.0 – Open a Terminal Session!

We'll be (mostly) working in the terminal for this so open up a new session.

The default MacOS __Terminal.app__ will work but consider installing [ITerm2].

It's more configurable and has some nice features like panes, full-screen mode, and integrated `tmux` ([among other things](https://iterm2.com/features.html)).

You can open either by finding the app in __/Applications__ or use Spotlight and type in the application name.

## 2.0 – Install XCode Command Line Tools

```bash
# Check if they are installed
xcode select -p

# Should output something like:
# #/Library/Developer/CommandLineTools

# If not, input:
xcode-select --instal

# Follow install instructions
```

## 3.0 – Install Homebrew

Homebrew is a free and open-source software package management system that simplifies the installation of software on macOS<sup>[1](#footnote-1)</sup>.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Check installation
which brew

# Should output something like:
# /usr/local/bin/brew
```

## 3.1 – Configure .bash_profile for Homebrew

First time doing something like this? See: [Create a Bash Profile](#create-a-bash-profile).

In a terminal session...

```bash
# Open your .bash_profile
code ~/.bash_profile
```

In your editor, add the following to your .bash_profile and __SAVE__.

```bash
# Update PATH so packages installed by Homebrew  are found first.
export PATH=/usr/local/bin:$PATH
```

Back in the terminal...

```bash
# This will reload .bash_profile
# and give us the new settings
source ~/.bash_profile
```

## 3.2 – Install Packages (with Homebrew)

Now that `brew` is ready we can install a few of the required system packages.

We're going to install:

- Python 2 (latest)
- Python 3 (latest)
- Git (latest)
- Pipenv (latest)
- Node & NPM (latest)

In a terminal session...

```bash
# Install packages
brew install python2 python3 git pipenv node

# Test installs
# Comments after commands represent expected output

which python    # /usr/local/bin/python
which python3   # /usr/local/bin/python3
which git       # /usr/local/bin/git
which pipenv    # /usr/local/bin/pipenv
which node      # /usr/local/bin/node
which npm       # /usr/local/bin/npm
```

The important bit is `/usr/local/bin`. If that's missing, something went wrong. You can try restarting your terminal app/session and checking that PATH is set correctly.

In a terminal session...

```bash
# You should see /usr/local/bin near
# the beginning of the output.
echo $PATH

```

## 4.0 – Pipenv

[Pipenv] is a dependency manager for Python projects. If you’re familiar with Node.js’ __npm__ or Ruby’s __bundler__, it is similar in spirit to those tools.

Pipenv is recommended for collaborative projects as it’s a higher-level tool that simplifies dependency management for common use cases<sup>[2](#footnote-2)</sup>.

It has several advantages over [Virtualenv] and [Virtualenvwrapper]:

* You no longer need to use pip and virtualenv separately. They work together.
* Pipenv uses __Pipfile__ and __Pipfile.lock__ to separate dependency declarations.
* Hashes are used everywhere, always.
* Strongly encourage the use of the latest versions of dependencies.

## 4.1 – Configure .bash_profile for Pipenv

We need to add some minor configuration to Pipenv to make sure it works as we expect.

In a terminal session...

```bash
# Open your .bash_profile
code ~/.bash_profile
```

In your editor, add the following and __SAVE__.
```bash
export PIPENV_VENV_IN_PROJECT=True
export PIPENV_IGNORE_VIRTUALENVS=True
export PIPENV_SHELL_FANCY=True
```

Back in the terminal...

```bash
# This will reload .bash_profile
# and give us the new settings
source ~/.bash_profile
```

Wondering what those settings do? See: [Pipenv Config Docs](https://docs.pipenv.org/advanced/#configuration-with-environment-variables).

## 5.0 – Install Docker For Mac

Download [Docker For Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) and follow the installation instructions.

## 5.1 – Configure Docker Preferences

You may want to give Docker some additional memory, if your machine can spare it. This step is optional, but may improve performance.

After Docker is installed, you can access preferences by going to the top bar and clicking on the small whale icon and selecting __"Preferences.." > "Advanced"__

![Docker Menu](https://i.imgur.com/PwGopdi.png)

![Docker Advanced Prefs](https://i.imgur.com/frYLAyZ.png)


## Appendix

### Create a Bash Profile

Your __.bash_profile__ is usually located in  `/Users/<username>/.bash_profile`.

Can't find your .bash_profile? It may not exist yet and you'll may have to create it.

```bash
cd ~/
ls -la | grep bash_profile

# Should output something like
lrwxr-xr-x 1 <username>  staff 56 Mar  1 16:22 .bash_profile

# If not, input:
touch .bash_profile
```

You can open it easily with a number of tools:

```bash
# Open with vim
vim ~/.bash_profile

# Open with VisualStudio Code
code ~/.bash_profile

# Open with Sublime
subl ~/.bash_profile

# Open with Atom
atom ~/.bash_profile
```

---
<sup id="footnote-1">1</sup> : From [en.wikipedia.org](https://en.wikipedia.org/wiki/Homebrew_(package_management_software)).

<sup id="footnote-2">2</sup> : From [Python.org](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies).
