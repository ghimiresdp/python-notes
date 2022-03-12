- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# File Handling in Python

- Python is capable of handling or manipulating data stored in files.
- We can open a file using inbuilt `open()` function.
- While opening a file, we have to pass different modes as a parameter to specify what we're trying to do with the file.

## File Opening Modes

1. `r`: **Reading** mode
   - The default mode.
   - It allows you only to read the file, not to modify it.
   - When using this mode the file must exist.

2. `w`: **Writing** mode
   - It will create a new file if it does not exist, otherwise will erase the file and allow you to write to it.

3. `a`: **Append** mode
   - It will write data to the end of the file.
   - It does not erase the file, and the file must exist for this mode

4. `rb`: **Binary Reading** mode
   - same as `r` but reading is forced in binary mode.
   - This is also a default choice.

5. `wb`: **Binary Writing** mode
   - same as `w` but writing is forced in binary mode.

6. `ab`: **Binary Apend** mode
   - same as `a` but appending is forced in binary mode.

7. `r+`: **Reading** mode plus **Writing** mode at the same time
   - This allows you to read and write into files at the same time without having to use `r` and `w`.

8. `w+`: **Writing** mode plus **Reading** mode at the same time.
   - If the file does not exist, a new one is made. otherwise overwritten.

9.  `a+`: **Apend** mode
   -  similar to `w+`

11. `rb+`: **Binary Reading** mode
     -  same as `r+` mode but forced in binary mode

12. `wb+`: **Binary Writing** mode
    -  same as `w+` mode but forced in binary mode

13. `ab+`: **Binary Apend** mode
    -  same as `a+` mode but forced in binary mode

## Opening and closing a file in python
- We use `open()` function to open the file.
- We use `file.close()` method to close the file.

**Basic Syntax**
```python
file_obj = open(filename, mode)
# do our stuff over here
file_obj.close()
```

## Reading a file

```python
file = open("my_file.txt", "r")
file.read()
file.close()
```

### The newer approach using `with` keyword.
- If we open the file with `with` keyword, then we do not need to explicitly close the file.
- It automatically closes the file whenever it goes out of the scope.

```python
with open(filename, 'r') as f:
    # do our stuff here
    f.read()
print("At this point, the file is closed")
```

## Writing into a file
```python
with open(filename, 'w') as f:
    f.write(filedata)
```


## Appending into a file
```python
with open(filename, 'a') as f:
    f.write(filedata)
```


## Reading a file line by line

```python
with open (filename, 'r') as f:
    for line in f:  # or  # for line in f.readlines()"
        print(line)
```
