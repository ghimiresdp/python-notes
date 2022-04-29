- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# Introduction to Virtual environments

Let us consider that we have to work simultaneously on 2 different projects with different package dependencies as follows

### **Base Python**
- `django==4.0.0`

### **Project 1**
- `django==2.2`
- `pillow==7.0`
- `numpy==1.0.0`


### **Project 2**
 - `django==3.2.10`
 - `pillow==9.1.0`
 - `numpy==1.5.0`

Suppose we have base python `3.9` installed and different requirements for different projects. Switching back and forth between the projects requires installing and uninstalling different packages which is impractical in daily use.


To avoid frequent installation and uninstalling of packages, we can use virtual environments.


A Virtual Environment is a tool that keeps dependencies required by different projects in separate places.


Followings are common virtual environments:

- `venv`, `virtualenv`
- `pipenv`
- `direnv`
- `pyenv`
- `conda`
