[Docker for Mac]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Docker]: https://docs.docker.com/docker-for-mac/install/  "Download Docker for Mac"
[Node & Npm]: https://nodejs.org/en/download/ "Intsall Node"
[Homebrew]: http://brew.sh/ "Homebrew Homepage"
[Virtualenv]: https://virtualenv.pypa.io/en/stable/ "Virtualenv Docs"
[Virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/ "Virtualenvwrapper Docs"
[Pipenv]: https://docs.pipenv.org/ "Pipenv Docs"
[Pyenv]: https://github.com/pyenv/pyenv "Pyenv Docs"
[NVM]: https://github.com/creationix/nvm "NVM Docs"
[Git]: https://example.com "Git Homepage"
[Python]: https://example.com "Python Homepage"
[Iterm2]: https://iterm2.com/downloads.html "Iterm2 Downloads"
[Bash]: https://www.gnu.org/software/bash/ "Bash Homepage"

# MacOS Setup

> NOTE: The following assumes a novice-level when configuring various preferences for MacOS. If you've got more experince and have already customized your machine simply review this document and ensure your machine meets all the requirements.

## Purpose

Document a _base-line_ OSX machine/environment for Python/Django/HTML5 development.


## Contents

- [System Requirements](#system-requirements)
- [What We'll Install](#what-we-will-install)
- [1.0: Install Docker For Mac](#10-install-docker-for-mac)
- [2.0: Open a Terminal Session!](#20-open-a-terminal-session)
- [3.0: XCode Command Line Tools: Install](#30-xcode-command-line-tools-install)
- [4.0: Homebrew Install](#40-homebrew-install)
    - [4.1: Homebrew: Configure ENV](#41-homebrew-configure-env)
    - [4.2: Homebrew: Install Packages)](#42-homebrew-install-packages)
- [5.0: Pyenv: Install Python](#50-pyenv-install-python)
- [6.0: Pipenv: Configure ENV](#60-pipenv-configure-env)
- [7.0 NVM: Install](#70-nvm-install)
    - [7.1: NVM: Install Node & NPM](#71-nvm-install-node-&-npm)
- [Appendix](#appendix)
    - [Create a Bash Profile](#create-a-bash-profile)


## System Requirements

- MacOS
- XCode Commandline Tools
- A Terminal Client with `bash` (or compatible shell)

## What We Will Install
- [Docker]
- [Homebrew]
    - [Bash]
    - [Git]
    - [Pyenv]
    - [Pipenv]
        - [Python] (3.6)
- [NVM]
    - [Node & Npm]

## 1.0: Install Docker For Mac

Download [Docker For Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) and follow the installation instructions.

## 2.0: Open a Terminal Session!

The default MacOS __Terminal.app__ will work but consider installing [ITerm2].

We'll be (mostly) working in the terminal for this so open up a new session. You can open either by finding the app in __/Applications__ or use Spotlight and type in the application name.

## 3.0: XCode Command Line Tools: Install

XCode Command Line Tools installs a subset of MacOS's XCode Software that includes useful/necessary utilities like GCC Compiler <sup>[1](#footnote-1)</sup>.

```bash
# Check if they are installed
xcode select -p

# Should output something like:
# #/Library/Developer/CommandLineTools

# If not, input:
xcode-select --install

# Follow install instructions
```

## 4.0: Homebrew Install

Homebrew is a free and open-source software package management system that simplifies the installation of software on macOS<sup>[2](#footnote-2)</sup>.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Check installation
command -v brew

# Should output something like:
# /usr/local/bin/brew
```

## 4.1: Homebrew: Configure ENV

First time doing something like this? See: [Create a Bash Profile](#create-a-bash-profile).

In a terminal session...

```bash
# Open your .bash_profile
# NOTE: `code` is the alias for the VisualStudio Code app.
#        Other editors like, SublimeText (`subl`), also expose similar aliases.
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

## 4.2: Homebrew: Install Packages

Now that `brew` is ready we can install a few of the required system packages.

We're going to install:

- [Bash] (latest)
- [Git] (latest)
- [Pipenv] (latest)
- [Pyenv] (latest)

In a terminal session...

```bash
# Install packages
# If you're interested, here are other useful packages: vim wget jq bash-completion
brew install bash git pipenv pyenv

# Test installs
# NOTE: Comments after commands represent expected output

command -v bash      # /usr/local/bin/bash
command -v git       # /usr/local/bin/git
command -v pipenv    # /usr/local/bin/pipenv
command -v pyenv     # /usr/local/bin/pyenv
```

The important bit is `/usr/local/bin`. If that's missing, something went wrong. You can try restarting your terminal app/session and checking that PATH is set correctly.

In a terminal session...

```bash
# You should see /usr/local/bin near
# the beginning of the output.
echo $PATH

```

## 5.0: Pyenv: Install Python

[Pyenv] lets you easily switch between multiple versions of Python.

We're going to install:

- [Python] (3.6.7)

In a terminal session...

```bash
# Run pyenv --help for more info about pyenv
pyenv install 3.6.7
```

## 6.0: Pipenv: Configure ENV

[Pipenv] is a dependency manager for Python projects. If you’re familiar with Node.js’ __npm__ or Ruby’s __bundler__, it is similar in spirit to those tools.

Pipenv is recommended for collaborative projects as it’s a higher-level tool that simplifies dependency management for common use cases<sup>[3](#footnote-3)</sup>.

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

## 7.0 NVM: Install

Node Version Manager ([NVM]) lets you easily switch between multiple versions of Node and NPM.

Unfortunately, NVM does not support a `brew` install so we have to run this instead (See [NVM] for additional info).

In a terminal session...

```bash
# NOTE: v0.33.11 was the version when this doc was written.
#       See https://github.com/creationix/nvm/tree/master
#       for latest install command.
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

## 7.1: NVM: Install Node & NPM

Next, We're going to install:

* [Node & NPM] (Latest LTS)

In a terminal session...

```bash
# Run nvm --help for more info about nvm
# NOTE: The NVM `install` command installs both Node and NPM
nvm install --lts
```

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
<sup id="footnote-1">1</sup> : Here's some useful info about [XCode Command Line Tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).

<sup id="footnote-2">2</sup> : From [en.wikipedia.org](https://en.wikipedia.org/wiki/Homebrew_(package_management_software)).

<sup id="footnote-3">3</sup> : From [Python.org](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies).
