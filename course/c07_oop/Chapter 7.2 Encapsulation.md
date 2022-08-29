- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 7.2 Encapsulation

**Table of contents**:


## Introduction

Encapsulation is the process of restricting the direct access to the data.
It can be achieved by binding the private attribute along with methods to make
the data usable. In python we make the data protected by naming the attributes
and methods starting with single underscore`_` or double underscores `__`.

The methods that are bound with protected attributes are called as getters and
setters. the **getter** method takes no arguments and **setter** takes one
argument except `self`.

**Why do we use Getters and Setters instead of public attributes?**

- It helps hiding or prevents modifying the state of the structured data
  preventing the unauthorized access.
- Suppose changing the state of an attribute should affect another attribute,
  the user modifying the public attribute might forget to reflect changes in
  the another.


**example**
```python
class MyClass:
    # protected attribute (accessible from outside of class)
    _name = 'Unknown'

    # private attribute (not accessible from outside of class)
    __age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        # Here, the state of _name is also influenced by the private attribute
        # __age.
        self._name = f'Unknown: {age}'

c1 = MyClass()

# print(c1.__age)
# raises an exception saying no attribute

print()

c1.set_age(30)
# here the age is set to 30 and also the state _name is changed accordingly.

print(c1.get_age()) # 30

# We can access the protected member if it starts with a single _
print(c1._name)     # Unknown: 30
```

