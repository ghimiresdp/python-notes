# Virtual environments

A Virtual Environment is a tool that keeps dependencies required by different projects in separate places.

Let us consider that we have to work simultaneously on 2 different projects with different package dependencies as follows


### **Project 1**
- `django==2.2`
- `pillow==7.0`
- `numpy==1.0.0`


### **Project 2**
 - `django==3.2.10`
 - `pillow==9.1.0`
 - `numpy==1.5.0`

Suppose we have base python 3.9 installed and different requirements for different projects. Switching back and forth between the projects requires installing and uninstalling different packages which affects performance of the work.


To avoid frequent installation and uninstalling of packages, we can use virtual environments. Followings are common virtual environments:

- virtualenv
- venv  (python's default virtual environment library)
- pipenv    (Better Alternative)


## Installing Virtual environment packages:
If you're using windows, the package `venv` is installed along with python (since 3.7)

for some linux systems, you need to install `venv` package to make it available globally by using the following command:

```shell
$ sudo apt install python3-venv
```

If we want to install `virtualenv`, `pipenv` or other environment wrappers, you need to install it.

```shell
$ pip install virtualenv
$ pip install pipenv
```


## Creating Virtual Environments
We can create virtual environment with `venv` command with the directory name (generally `venv`, `env`, `project_env`, etc) as an argument.

`python -m venv <venv_folder_name>`

```shell
# if venv is in path
$ venv venv

# if specific python is to be selected
$ python -m venv venv   # or
$ py -m venv venv       # windows

$ python3 -m venv venv

# windows only
$ python -3.9 -m venv venv
```

with `virtualenv`, we can run `virtualenv venv` to get similar results.

Above command creates the folder `venv` inside the working directory that contains the copy of the base python interpreter.


## Activating the virtual environment
Once the virtual environment is created, we need to activate the virtual environment so that the python executable created with the virtual environment gets selected.

To activate the virtual environment, we need to run either of the following commands based on your operating system.

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

## Knowing if venv is activated
The first and the easiest way to know that your environment is activated is to look at the shell, which would show shell similar to  `(venv) path/to/cwd`

We can also run the command `which python` to know which python executable is used for the current shell in some shells.

Once the virtual environment is activated, you have no longer access to the packages that are installed in the base-python. you need to install them inside the virtual environment so that all the packages are isolated inside the environment. This overcomes the problem of incompatibitilies along the project.

You can check installed packages using `pip freeze` command which will show you currently installed packages inside the active virtual environment.
> - remember, the command `pip freese` will not show you any packages installed outside of the virtual environment.
> - but you can access global packages and executables even if you haven't installed them inside the virtual environment.


## Deactivating the virtual environment
We can just enter `deactivate` command in any shell/ terminal to deactivate the current virtual environment.

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
