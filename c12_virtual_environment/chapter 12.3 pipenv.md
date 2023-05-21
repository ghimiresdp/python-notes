- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 12.3. `pipenv` and its usage

- [12.3. `pipenv` and its usage](#123-pipenv-and-its-usage)
  - [PIPENV features](#pipenv-features)
  - [Installing Pipenv](#installing-pipenv)
  - [Creating a new virtual environment](#creating-a-new-virtual-environment)
  - [Activating virtual environment](#activating-virtual-environment)
  - [Installing packages and dependencies using pipenv](#installing-packages-and-dependencies-using-pipenv)
  - [Uninstalling packages using pipenv](#uninstalling-packages-using-pipenv)
  - [Checking dependency graph using pipenv](#checking-dependency-graph-using-pipenv)

source: https://docs.python.org/3/library/venv.html

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment.

## PIPENV features

Some of the features of pipenv are as follows:

- `pip` and `virtualenv` are unified so that we do not need to use them separately.
- Dependencies are managed using a `Pipfile` and `Pipfile.lock` is used to separate abstract dependency declarations from the last tested combination.
- It allows user to declare *dependencies* and *dev-dependencies* which is a way better than managing dependencies with `requirements.txt`.
- It automatically loads `.env` file so that the development workflow is even easier with environment variables.

## Installing Pipenv

If we have python and pip installed, it is easier to install pipenv.

```shell
$ pip install --user pipenv
```

to upgrade pipenv, we can use the command below:

```shell
$ pip install --user --upgrade pipenv   # or
$ pip install --user -U pipenv
```


## Creating a new virtual environment

We can create a new virtual environment  using the command below:

```shell
$ pipenv install
```

The command above will create a virtual environment in `$HOME/.virtualenvs/project_name` folder.

if we want to install pipenv in the working directory, we have 2 options.

1. create an empty directory named `.venv` and run `pipenv install`
2. set the environment variable `PIPENV_VENV_IN_PROJECT=1` in your operating system and run `pipenv install` command.

by doing this, `pipenv` installs a new virtual environment inside `.venv` directory of the current folder.


## Activating virtual environment
We actually do not need to activate virtual environment when using pipenv since it automatically checks whether the virtual environment is created for the project or not and selects the interpreter itself.

If we want to activate the virtual environment anyways, we can run:

```shell
$ pipenv shell
```
which automatically activates the virtual environment.

We can then deactivate the virtual environment using:
```shell
$ exit
```
The above command deactivates the virtual environment.


## Installing packages and dependencies using pipenv

unlike `venv` or `virtualenv`, we do not need to activate virtual environment to install packages.

We can install packages using the command:

```shell
$ pipenv install package_name
```

or we can specify the version using:

```shell
$ pipenv install package_name==version
```

The above command installs packages and dependencies and updates both `Pipfile` and `Pipfile.lock` file so that we do not need to create or update `requirements` file.

We can traditionally install packages using `pip install package)name` command also, but it do not update the `Pipfile` and `lock` file so doing this is discouraged when using Pipenv.


## Uninstalling packages using pipenv

We can uninstall packages using the command below:

```shell
$ pipenv uninstall package_name

$ pipenv uninstall package_1 package_2  # multiple packages

```

THe above command removes the package, its dependencies and updates both `Pipfile` and `Pipfile.lock`.


## Checking dependency graph using pipenv

Another Amazing feature of pipenv is that it is able to show dependency graph so that you will be able to know the package and their dependencies too.

we can check the dependency graph using the command below:

```shell
$ pipenv graph
```

The command above shows all the dependencies and their dependencies in the console. The example output is as follows:

```shell
$ pipenv graph

djangorestframework==3.13.1
  - django [required: >=2.2, installed: 4.0.3]
    - asgiref [required: >=3.4.1,<4, installed: 3.5.0]
    - sqlparse [required: >=0.2.2, installed: 0.4.2]
    - tzdata [required: Any, installed: 2022.1]
  - pytz [required: Any, installed: 2022.1]
Pillow==9.1.0
```
You can see the package `djangorestframework` of version `3.13.1` is installed which requires `django` of version `>=2.2` and installed version is `4.0.3`.

similarly the dependencies of `django` are `asgiref`, `sqlparse`, `tzdata` are installed.
