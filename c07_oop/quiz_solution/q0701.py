"""
© https://sudipghimire.com.np

Create a python class with following properties:

1. private class attribute
2. public class attribute
3. instance attribute
4. initializer method
5. string representation method [__str__()]
"""

# This is the example solution you can create on your own style
class MyClass:
    var_1 = 5       # 2
    __var_2 = 10    # 1

    def __init__(self): # 4
        self.var_3 = "Hello"    # 3

    def __str__(self) -> str:   # 5
        return f"MyClass with var3: {self.var_3}"
