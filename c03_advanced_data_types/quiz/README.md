# Chapter 3 Advanced Data Types and Operations Quiz

Please read the note carefully and try to solve the problem below:

**Table of Contents**:

- [Chapter 3 Advanced Data Types and Operations Quiz](#chapter-3-advanced-data-types-and-operations-quiz)
  - [Quiz Q0301](#quiz-q0301)
  - [Quiz Q0302](#quiz-q0302)
  - [Quiz Q0303](#quiz-q0303)
  - [Quiz Q0304](#quiz-q0304)
  - [Quiz Q0305](#quiz-q0305)
  - [Quiz Q0306](#quiz-q0306)
  - [Quiz Q0307](#quiz-q0307)
  - [Quiz Q0308](#quiz-q0308)
  - [Quiz Q0309](#quiz-q0309)
  - [Quiz Q0310](#quiz-q0310)
  - [Quiz Q0311](#quiz-q0311)
  - [Quiz Q0312](#quiz-q0312)

## Quiz Q0301

Write a program to create an empty list named `my_list` and

1. Add numbers 5 and 9 to the list using `append()` method
2. Ask the user to input any number in the console and add the number to the list.
    - You can use `int()` to typecast string to integer if you want.
3. Create another list `more_items` with 3 items on it and extend the list `my_list` using `extend` method.
4. Now find the length of the list and print the length of list describing it in a sentence.
    - you can use string formatting for better outputs.
5. Now remove the second item using `pop()` method and see if the item exists in the list
    - you can print the list before and after using the `pop()` method.

**[Click](solution/q0301.py)** to see the solution

## Quiz Q0302

Write a program to add 5 different wild animals to a list named `wild`.

Example: tiger, lion, deer, bear, zebra

1. sort them in ascending using the `sort()` method.
2. reverse the list using the `reverse()` method.
3. now add 3 more animals to the list `wild`. Example: leopard, elephant, rhino
4. find the position of `leopard` using the `index()` method and remove it using `the pop()` method.
    - pop should have the index value returned using the `index()` method.
    - do not hard-code the position of leopard by manually counting it from the list.
    - check whether the leopard is removed from the list or not by `index()` method again. if the value error occurs,
      you have successfully removed it from the list. otherwise, try to do it again.
    - you can then comment the line that gives exception to continue to the next question.
5. Now add `leopard` again in the index `2` using `insert()` method.
6. Again, remove `rhino` from the list using remove() method.

Note: *you can check output after each successive operations.*

**[Click](solution/q0302.py)** to see the solution

## Quiz Q0303

Try creating a multi-dimensional list or nested list `multi` containing different numbers.

```py
Example:
[
    [12, 52, 37],
    [46, 51, 16],
    [17, 82, 39]
]
```

1. Access the number `51` from the list.
2. Access the number `82` using the negative indices.
3. Find out the length of the list `multi`
4. Append another list`[40, 61, 10]` inside the list `multi`. The final list should
   be: `[[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]`
5. Use foreach in the list `multi` to print each list item to the console.
    - **Bonus**: *Try using nested foreach to access each item inside of the inner list*
    - **Bonus**: *Try finding out the length of each inner list*
6. Finally clear the list `multi` using the `clear()` method and verify if the list is empty or not.

**[Click](solution/q0303.py)** to see the solution

## Quiz Q0304

Write a program to create a tuple to add 5 different numbers.

1. find out the length of the tuple
2. find out the 3rd element of the tuple by accessing it through the index
3. use `enumerate()` function to map each element with its *index* and print it using for loop.

## Quiz Q0305

Write a program to create a nested tuple and access different elements of the inner tuple using
positive and negative indexes.

## Quiz Q0306

create two different tuples `t1` and `t2` with different elements inside it
create the next tuple `t3` to add all values of t1 and t2 by destructuring or unpacking.

- suppose `t1` has `(1, 6, 9, 4, 3)`
- and `t2` has `(2, 7, 8, 3, 5)`
- `t3` must have `(1, 6, 9, 4, 3, 2, 7, 8, 3, 5)`

## Quiz Q0307

Write a program to create two different set of countries

1. **Rich**: USA, China, Japan, Germany, France, Australia, Italy
2. **Europe**: Germany, France, England, Switzerland, Italy, Portugal, Sweden

**Use Set methods to find out:**

1. countries that are rich but not in Europe
2. countries that are in Europe but not rich
3. countries that are both rich and are in Europe
4. countries that are either rich or in Europe, but not both
5. all the countries in either of the sets. (Names must be unique)
6. see if two sets are disjoint or not
7. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
    - hint: use `difference_update()` method. for more, please refer to python documentation
8. Create 2 more sets:
   1. `asian_rich`: China, Japan
   2. `american_rich`: USA, Canada
9. Check whether `asian_rich` is a subset of `rich` or not.
10. Check whether `rich` is a superset of `asian_rich` or not.
11. Check whether `american_rich` is a subset of `rich` or not.
**Note**: *you can use different operators to perform above operations*

## Quiz Q0308

Create a dictionary of a person that contains key value pair of

- name: `str`
- age: `int`
- profession: `str`
- married: `bool`

Set values with valid data types to each keys of the dictionary

1. Print the value of `'name'` from the dictionary
2. Add the age by `10` and print the dictionary items in formatted string
    Eg: `{name} will be {new_age} after 10 years`.
3. Try getting the value of `'employed'` from the dictionary.
    - If exception occurs, note it and check what exception says and finally comment the line.
4. try using `get()` method instead of large brackets `[]` in the previous question.
5. try using `get()` method with second parameter as `False` and see what is printed.
    Example: `person.get('employed', False)`

## Quiz Q0309

create a dictionary `car` with 3 keys `brand`, `model`, and `price`.

1. Set a random value to a new key `engine` in the dictionary.
2. Add 3 more keys (color, no_of_seats, transmission) using `update` method.
3. Remove the key `color` from the dictionary.
4. Try using `popitem()` method in the dictionary and see what changes in dictionary
5. Use `for` loop to iterate through all keys from a dictionary.
6. Use `for` loop to iterate through all keys from a dictionary using `keys()` method.
7. Use `for` loop to iterate through all values from a dictionary using `values()` method.
8. Use `for` loop to iterate through all keys, values from a dictionary using `items()` method.

## Quiz Q0310

1. Create a nested dictionary named yoda with following properties:
    - age: 910
    - species: Yodas
    - gender: male
    - affiliations: ['Jedi', 'Galactic Republic']
    - master: <dict>
        - name: Qui-Gon Jinn
        - age: 48
        - affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']
        - master: <dict>
            - name: Dooku
            - age: 83
            - affiliations: ['House Serenno', 'Jedi']
2. Print the value of the first affiliation of `Dooku` from the dictionary
3. Add new affiliation 'Sith' to Dooku
4. `pop` the key 'master' from the dictionary

## Quiz Q0311

1. create a variable `odd` with hinting as `int` and assign a value to it.
2. create a variable `PI` with hinting as `float` and assign 3.1415 to it.
3. create any variable with `string` type hinting and assign `integer` value to it.
    - Check whether the program gives error in execution or not and explain with reasons.

## Quiz Q0312

1. Suppose we have the variable assigned as follows:

    ```python
    PI = 3.1415
    ```

    I want to print the value of PI to be 3. How should I convert the data to an integer? Please Explain with code.

2. Suppose we have variables assigned as follows:

    ```python
    str_1 = "20"
    str_2 = "30"
    print(str_1 + str_2)
    ```

    above line gives us output of `"2030"` but I want the answer to be `50`. How would you solve the problem using type conversion?

3. Suppose we have variables assigned as follows:

    ```python
    x = ['1', '2', '3', '4', '5']
    sum = 0
    ```

    - I want the value of `sum` to be `15`.
    - **Hint**:
      - Use `for` loop in the list
      - Change the type from `str` to `int` in each iteration

4. Suppose we have variables assigned as follows:

    ```python
    odd = [1, 3, 5, 7, 9, 11, 13, 15]
    prime = [2, 3, 5, 7, 11, 13, 17]
    ```

    use type conversion to these lists to appropriate data type and find out
    - numbers that are odd but not prime
    - numbers that are either odd or prime
    - numbers that are prime but not odd.

Final values should be list and stored to respective variables.
