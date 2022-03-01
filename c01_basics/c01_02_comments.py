"""
© https://sudipghimire.com.np

Comments in python

- Comments are the lines or the part of code that is ignored by the python interpreter.
- If you want to describe what you're doing or what the line below states, you might want to add comments
  that makes other users easy to understand the code
- comments are not interpretted and contains no syntax inside the comment line
- comments can also be added after expressions
- Sometimes If some lines of codes are not necessary, we just comment the lines for future use

- Single line comments can be added using #
- multiline comments can be added using triple single or double quotes
"""

# This is a single line comment. When I go to next line the comment scope ends.
"""
This is a multiline comment.
I can write any lines of code inside these quotation marks and will
still be counted as comment
Multiline comment should be enclosed within triple single or double quotes
"""

print("Hello World!")  # Single line comment can be at the end of the statement too.


# Multiline comments can also be used as documentation purpose.
# Please ignore the structure of a program since we're going to learn this in the future
def add_me(a, b):
    """

    Parameters:

    - `a`: The first argument that can accept either integer or floating point numbers
    - `b`: The second argument that can accept either integer or floating point numbers

    Returns:

    the sum of 2 numbers `a` and `b`


    """
    return a + b
