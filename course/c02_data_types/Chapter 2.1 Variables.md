- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

# Chapter 2: Python Variables and Data Types

## Variables

let us suppose we have a statement as follows:

```python
x = 5
```

here, `x` is an identifier. It is also called as a variable since it's value can be changed while executing.

The above statement says, set the value `5` to the variable `x` somewhere in a memory. **Python Memory Manager** manages the location where the values are stored.

 There are few rules to create a variable name which are as follows:

1. Python identifiers can start with alphabetical characters.

   ```python
   # Example
   name = "John Doe"
   age = 20
   ```

2. They can start with underscore `_` character.

   variables starting with `_` are generally used as protected attributes.

   ```python
   # Example
   _name = "John Doe"
   _age = 20
   ```

3. Variables can not start with numeric characters but can exist in between or at the end.

   ```python
   # Example
   # 1name = "John Doe"       # incorrect identifier name
   name1 = "John Doe"       # correct syntax
   na1me = "John Doe"       # correct syntax
   ```

4. We can't use special characters like `space`, `tab`, `+`, `-`, etc.

   ```python
   # The following are not allowed
   """
   name one = "John Doe"       # incorrect identifier name
   name+one = "John Doe"       # incorrect identifier name
   name-one = "John Doe"       # incorrect identifier name
   """
   # instead, we can use underscore character to separate 2 words
   name_one = "John Doe"
   ```

5. We use `snake_case` for variable definition

   Even though python supports CamelCase identifier name, it is generally not recommended to use. PEP recommends using `snake_case` identifiers over other type.



Some examples of identifiers supported by python are as follows

```python
name = 'cow'            # valid
_name = 'cow'           # valid
name1 = 'cow'           # valid
name_1 = 'cow'          # valid
# name 1 = 'cow'        # invalid
Name = 'cow'            # valid but not recommended by PEP
first_name = 'John'     # valid
firstName = 'John'      # valid but not recommended by PEP
FirstName = 'John'      # valid but not recommended by PEP
```
