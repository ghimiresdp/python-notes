"""
© https://sudipghimire.com.np

Comprehension Exercises
"""

'''
1. convert the following loop to list comprehension
'''
list = []
for x in range(10):
    list.append(2*x+1)

# Answer Here


'''
2.  Generate a dictionary from a list of first 10 numbers and it's square values
    using dictionary comprehension.

    Final value should be in format: {1:1, 2:4, 3:9, 4:16, ..., 10, 100}
'''
# Answer Here

'''
3.  Create the following pattern using list comprehension, `join()` method, and others if needed.
    Try to solve in a single line or single statement.

    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
'''
# Answer Here

'''
4.  A mathematical function is defined by y = (4x ** 2) + (3 * x) - 6
    i. Create a generator function to generate first 1000 integers starting from -100 and store to a variable y.
    ii. Create a list using list comprehension to generate the same values
    iii. Compare the memory usage by those variables created in steps (i) and (ii) using __sizeof__() method.
    iv. Try to generate values of y for first million integers and compare memory usage as done in step (iii).

    To learn more about __sizeof__() method, please visit https://www.javatpoint.com/sizeof-in-python
'''
# Answers


'''
5.  Write a program to split a string 'Apple' into a dictionary of
    ASCII values of each characters using comprehension methods.

    To learn more about ASCII please refer to the site https://www.asciitable.com/

    Use the `ord()` method to find out the ASCII values

    final output should be: {'A': 65, 'p': 112, 'l': 108, 'e': 101}
'''
# Answer Here

'''
6.  Write a program to generate a dictionary from the given nested tuple using dictionary comprehension.
'''
abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
)
# Answer Here


'''
BONUS EXERCISES

7.  Try All of the pattern generation exercises (if possible) with list comprehension
'''
# ANSWERS HERE
