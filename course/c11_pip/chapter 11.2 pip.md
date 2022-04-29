- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 11.2. Dependency management in Python

There are various dependency management tools available in python. some of them are `pip`, `conda`, `poetry`, etc. `pip` comes by default with python and is used as the default package manager by majority of developers and companies while `conda` is popular among data scientists with little exposure in software development.

# The `pip` package manager
- It is a python package manager that comes along with python.
- It is also known as Dependency Management system
- It is going to install/ uninstall specific version of softwares to your environment.
- example: `PIP` `conda`

In this session, we're going to use `PIP`
PIP comes along with python.
PIP is the standard or default package manager for python.

## checking if pip is installed

If it is installed, it would show you the version number along with the path of the executable

```shell
$ pip --version

pip 21.3.1 from C:\Users\user\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)
```
 in some linux OS, you might need to use `pip3` instead of `pip`


If the pip is not installed, we would see the error message.
If you're using windows and you installed python, it automatically installs pip by default

 ```shell
 $ pip --version

Command 'pip' not found, but can be installed with:

sudo apt install python3-pip
```

## Installing new packages
- We use `pip install [package_name]` to install the package to our existing environment.
- Sometimes we want to install specific version of the package, in that case we use `pip install [package_name]==[version_name]`
- To install the packages in range, we can use symbols such as `==`, `<=`, `>=`, `~=`, etc.
- We can even use Wildcards (eg: `1.2.*` ) to install packages

The following are examples to install django with `pip`:

```shell
$ pip install django    # installs the latest release

$ pip install Django==3.2.12  # installs the specific release

$ pip install Django~=3.2   # installs the latest patch of the equivalent django release

$ pip install Django>=3.2  # installs the optimum version of djano greater than 3.2

$ pip install Django<3.3  # installs the most recent version of django less than 3.3

$ pip install Django==3.2.* # installs the latest patch release of django 3.2
```


## Checking the list of installed packages
We can use `pip list` or `pip freeze` commands to list out the installed packages.

### `pip list`
```shell
$ pip list

Package                      Version
---------------------------- ---------
absl-py                      1.0.0
anyio                        3.5.0
argon2-cffi                  21.3.0
argon2-cffi-bindings         21.2.0
asgiref                      3.4.1
Django                       3.2.12
```

### `pip freeze`
```shell
$ pip freeze

absl-py==1.0.0
anyio==3.5.0
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
asgiref==3.4.1
Django==3.2.12
```
 we can export current installed packages to the `requirements.txt` file so that we can install the same version of packages in the future.

 ### Exporting the list of packages with `pip freeze`
 sometimes we install so many packages so that we can not remember the packages and their versions while installing, so we want to store them in a special files called `requirements.txt`. We can use any filename but `requirements.txt` is the standard and the syntax is highlighted by different IDEs and code editors.

 ```shell
 $ pip freeze > requirements.txt
```
The above command saves all the requirements to the file `requirements.txt` from the current environment.

```toml
absl-py==1.0.0
anyio==3.5.0
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
asgiref==3.4.1
Django==3.2.12
```

## Installing packages from requirements.txt
We can install packages from the requirements file using the command `pip install -r [path/to/the/requirements.txt]`

```shell
$ pip install -r requirements.txt
```

## Upgrading the previously installed package

If we want to upgrade the current version of packages then we can install the newer version with the following methods:

- `pip install [package]==[new_version_number]` command with the specific release version
- `pip install -U [package]` command.

When we try to run above commands, the older versions gets uninstalled and the newer version gets installed.

Suppose we have installed django of version `3.2.10`, and want to install the latest one, then we can run the following commands.

```shell
$ pip install Django==4.0.0 # uninstalls 3.2.10 and installs 4.0.0 version of django

$ pip install -U Django # uninstalls 3.2.10 and installs the latest version of it.
```

### Uninstalling packages

To uninstall python packages, we can  use `pip uninstall [package_name]` command.
For example, if we want to uninstall `django` package, we can run the following command:

```shell
$ pip uninstall django
```

since only one version of the package gets installed, we do not need to specify the version of the package to be uninstalled.

