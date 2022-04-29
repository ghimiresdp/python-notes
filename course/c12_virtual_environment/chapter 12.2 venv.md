- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 12.2. `venv` and its usage
ref: https://docs.python.org/3/library/venv.html

The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories.

## Installing `venv` in our system:
If We're using windows&reg;OS, the package `venv` is installed along with python with newer versions

for some linux systems, you need to install `venv` package to make it available globally by using the following command:

```shell
$ sudo apt install python3-venv
```

## Creating Virtual Environments
We can create virtual environment by `venv` command with the first argument as directory name (generally `venv`, `env`, `project_env`, `.venv`, etc) as an argument.

`python -m venv <venv_folder_name>`

```shell
# if venv executable is in path
$ venv venv

# if specific python is to be selected,
$ python3 -m venv venv      # or
$ python3.7 -m venv venv   # or
$ py -3.7 -m venv venv       # windows
```

with `virtualenv`, we can run `virtualenv venv` to get similar results.

Above command creates the folder `venv` inside the working directory that contains the copy of the base python interpreter with no external dependencies installed at first.

Once the virtual environment is created and activated, it will work as a fresh install of a python programming language.

## Activating the virtual environment
Once the virtual environment is created, we need to activate the virtual environment so that the python executable created with the virtual environment gets selected.

To activate the virtual environment, we need to run either of the following commands based on our operating system.

**Windows with cmd or powershell**
```cmd
C:\dev\my-project> venv\Scripts\activate

(venv) C:\dev\my-project>
```

**Linux or mac or unix-based OS or git-bash on Windows**
```shell
$ source venv/bin/activate  # linux or mac

$ source venv/Scripts/activate  # windows with git bash


(venv) /dev/my-project
$
```
_Note On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:_
```powershell
PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

See About Execution Policies for more information.

## Knowing if `venv` is activated
The first and the easiest way to know that your environment is activated is to look at the shell, which would show shell similar to  `(venv) path/to/cwd`

We can also run the command `which python` to know which python executable is used for the current shell in some shells.

Once the virtual environment is activated, you have no longer access to the packages that are installed in the base-python. you need to install them inside the virtual environment so that all the packages are isolated inside the environment. This overcomes the problem of incompatibitilies along the project.

You can check installed packages using `pip freeze` command which will show you currently installed packages inside the active virtual environment.
- _remember, the command `pip freeze` will not show you any packages installed outside of the virtual environment_.
- _but you can access global packages and executables even if you haven't installed them inside the virtual environment_.


## Deactivating the virtual environment
We can just run `deactivate` command in a virtual environment shell/ terminal to deactivate the current virtual environment.

**Windows**
```cmd
(venv) C:\dev\my-project> deactivate

C:\dev\my-project>

```

**linux/Mac**
```shell

(venv) /dev/my-project
$ deactivate

/dev/my-project
$
```
