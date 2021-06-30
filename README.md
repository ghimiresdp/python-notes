# python-level1
A repository for Python Level 1 course, content, and lab exercises.

The course has the folder structure as follows:

```
|-- exercises
|    |-- 01_basics.py
|    |-- 02_variables.py
|-- res
|    |-- 01_basics.pdf
|    |-- 02_variables.pdf
|  ...
|
|-- src
|    |-- 01_basics
|    |    |-- 01_hello_world.py
|    |
|    |-- 02_data_types
|    |    |-- 01_variables.py
|    |    |-- 02_numbers.py
|    |  ...
.    .
.    .
.    .
```

If you want to practice exercises contained in this repo then please `fork` this repository to your own account and modify as per your requirements.

> I suggest you not to make any changes in the `main` branch in your repository too so that you can pull and rebase future changes to your `fork`.

### Pulling future changes

for pulling the future changes you can add `remote` in your local repository with the commands below:

1. Add remote to your local repository
    ```
    git remote add upstream https://github.com/ghimiresdp/python-level1.git

    ```

1. Fetch the changes to your local repository

    ```
    git fetch upstream
    ```

1. checkout to the main branch

    ```
    git checkout main
    ```


1. After fetching, simply merge or rebase your code with either of the commands below:

    - ```
      git rebase upstream/main
      ```
        or
    - ```
      git merge upstream/main
      ``` 


1. Push to your remote repository

    ```
    git push origin main
    ```