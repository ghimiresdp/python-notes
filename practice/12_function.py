'''
1.  Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
    according to the customer's requirements.

    The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
    Please use the `make_coffee()` function below to prepare a coffee and serve it.

    Followings are the ingredients for coffee:

    Sugar: no. of spoons
    beans: no. of spoons
    milk: volume in ml.

    The total volume of coffee should be 250ml. The maximum volume of milk can be only upto  150ml. greater than that
    should give the error saying not acceptable.

    Finally print the line describing the coffee you prepared along with  milk and water composition.



'''


def make_coffee(sugar: int, beans: int, milk: int):
    pass


"""
2.  Write a program to create a multiplication table of the given number.


Example:

Enter a number: 13

Multiplication table for 13

| 13  X   1|    13|
| 13  X   2|    26|
| 13  X   3|    39|
| 13  X   4|    52|
| 13  X   5|    65|
| 13  X   6|    78|
| 13  X   7|    91|
| 13  X   8|   104|
| 13  X   9|   117|
| 13  X  10|   130|

"""
# Answer Here


"""
3.  Create a function that takes
    - width: float
    - height: float (optional)
    for a rectangle. If height is not provided, then consider it as a square and return its area and perimeter.
"""


def area_perim(width: float, height: float = None):
    # your answer here
    pass


area1, per1 = area_perim(5.5, 7.8)

area1, per1 = area_perim(10.2)


"""
4.  Write a python function to print the sum of double of numbers provided as arguments.
    You can pass any arguments as possible but the function should return the answer without
    giving any error if correct data type is passed as arguments.

"""
# Answer Here


"""
5.  Create a lambda function and use it to find x**2 + 3x -10 from a list and save it to another list.

"""
# Answer Here


"""
6.  Write a program that accepts an integer and prints out the sum of all numbers from 1 upto that number in a list.
    You have to use a recursive function to achieve the summation.

    Eg: if you enter 5, the answer would be 5 + 4 + 3 + 2 + 1 = 15

     you do not need to print all the values to add, the final value should be 15 if yoou enter 5. try it for 10 and
     check whether if gives 55.
"""
# Answer Here


"""
7.  Write a program to print the first n numbers of a fabbonnacci series using a recursive function
    Fabbonnacci series is a series where a number is equal to the sum of the previous 2 numbers.

    some numbers in the fabbonnacci series are as follows:
    1   1   2   3   5   8   13  21  ...

    - here first and second numbers are always 1 and 1
    - 3rd  =  1st + 2nd   =   1 + 1   =   2
    - 4th  =  2nd + 3rd   =   1 + 2   =   3
    - 5th  =  3rd + 4th   =   2 + 3   =   5
     and so on

    the final output should look like:

    The first 10 fibbonnacci number is:  1 1 2 3 5 8 13 21 34 55
"""
# Answer Here


def fabbonnacci(num, a=1, b=1):
    pass


fabbonnacci(20)

"""
8.  Write a program to create a function that takes an arbritrary number of parameters as integer values and perform
    y = x**2 + 3x + 5
    return the list of pairs in the form of [(x1, y1), (x2, y2), (x3, y3)]

    example:

    >> find_y(1, 2, 3)
    >> [(1, 9),(2, 15),(3, 23)]
"""
# answer here


"""
BONUS 1.  Write a program that prints out the first n rows of pascal's triangle.

Example:

Enter a number: 5

           1
         1    1
      1    2    1
    1    3    3    1
 1    4    6    4    1

Enter a number: 9

                     1
                   1    1
                1    2    1
              1    3    3    1
           1    4    6    4    1
        1    5    10    10    5    1
     1    6    15    20    15    6    1
  1    7    21    35    35    21    7    1
1    8    28    56    70    56    28    8    1


Hint:
- inside a function, create an empty list `lst`
- create a loop from 1 upto number you entered
- create a list `tmp` of [1] * n where n is the value of the current iteration.
    this will create
    [1]           in the first iteration
    [1, 1]        in the second iteration
    [1, 1, 1]     in the third iteration and so on.

    - in each iteration check whether the list has length greater than 2 or not

    - if the length of the list is greater than 2, update the values as follows:
        create another loop of value of range(1, lst.__len__())
            update tmp[x] = array[x] + array[x]-1
    - finally update lst = tmp
    - print all the values of the list using string formatting methods.
    - you can center the text using 'str'.center(50) method or evaluate the number from the value user enters

"""
