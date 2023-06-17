> - **created by**: Sudip Ghimire
> - **URL**: https://www.sudipghimire.com.np
> - **GitHub**: https://github.com/ghimiresdp
>
> [go to course contents](https://github.com/ghimiresdp/python-notes/)

# Chapter 12.4: Poetry

**Table of Contents:**

- [Chapter 12.4: Poetry](#chapter-124-poetry)
    - [Introduction](#introduction)
    - [Installation](#installation)
    - [Basic Usage](#basic-usage)
        - [Setting up a new project](#setting-up-a-new-project)
        - [Setting up existing project](#setting-up-existing-project)
        - [Activating the virtual environment](#activating-the-virtual-environment)
        - [Adding/Installing new package](#addinginstalling-new-package)

## Introduction

**Poetry** is an advanced packaging as well as dependency management tool that
allow users to easily manage the virtual environment, add dependency, dev-
dependency, lock packages, as well as package a library. Poetry requires python
version of at least `3.7` to work.

It generally uses a configuration file called `pyproject.toml` in the working
directory that defines dependencies and locks all the dependencies and their
peer dependency in a lockfile called `poetry.lock`

**Sample `pyproject.toml` file:**

```toml
[tool.poetry]
name = "My Project"
version = "0.1.0"
description = ""
authors = ["John doe(johndoe@example.com)"]
readme = "README.md"
packages = [{ include = "lib" }]

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## Installation

The easiest way to install poetry is to use `pip` command

```shell
pip install poetry
```

If you are an advanced user or having any issues while installing, you can
follow instructions in the official documentation
<https://python-poetry.org/docs/#installing-with-the-official-installer>.

If your installation is successful, you would see the version of poetry if you
run command:

```shell
poetry --version
```

```shell
Poetry (version 1.5.1)
```

## Basic Usage

> **Note**: To know more about using poetry, you can check the official docs:
> <https://python-poetry.org/docs/basic-usage/>

### Setting up a new project

We can setup a new project with `new` command.

```shell
poetry new my-project
```

### Setting up existing project

We can use poetry `init` command to initialize poetry to an existing project.

```shell
# change the CWD to an existing project if not
cd <your-project-directory>
poetry init
```

### Activating the virtual environment

We can activate the virtual environment by running poetry `shell` command.

```shell
/path/to/workspace
$ poetry shell
Spawning shell within /path/to/.venv

(my-project-py3.10) /path/to/my/workspace/
$
```
Activating the virtual environment with `poetry shell` command automatically
adds the environment variables from `.env` file if it exists.

After activating the virtual environment, we can use poetry as a regular `pip`
package except for adding packages.

### Adding/Installing new package

We can easily update the `[tools.poetry.dependencies]` section of `pyproject.toml`
file to add a new dependency and run `poetry install` command.

We can also easily use poetry `add` command to add new package

```shell
poetry add requests
```

