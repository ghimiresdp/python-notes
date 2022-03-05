# PROJECT: A Hangman Game

## prerequisites:
- Python Level 1 Course upto Chapter 7
- `random` library

## Instruction

Create a Hangman game that Generates a random word from a list as shown below:

- COMPUTER
- PROGRAMMING
- INHERITANCE
- POLYMORPHISM
- DICTIONARY
- COMPREHENSION
- LAMBDA
- ITERATION

### The program should start by asking a user name and showing a random greeting out of 3:

- We are so excited to have you on our team, John!
- We are thrilled to have you at our terminal, John!
- Welcome John!! lets start the exciting game


After welcoming the random word is selected and displayed with random

**Sample Welcome Screen:**
```
     ////    ////     ///////    ////    ////    /////////
    ////    ////   ////   ////  //////  ////   ////    ////
   ////////////  ////////////  /////// ////  ////
  ////////////  ////////////  //// ///////  ////   ///////
 ////    ////  ////    ////  ////  //////    ////    ////
////    ////  ////    ////  ////   /////     //////////


     ////        ////     ///////    ////    ////
    //////    //////   ////   ////  //////  ////
   ////////////////  ////////////  /////// ////
  ////  ////  ////  ////////////  //// ///////
 ////        ////  ////    ////  ////  //////
////        ////  ////    ////  ////   /////

===========================================================
Please Enter your name: John

===========================================================

Welcome John!! lets start the exciting game
===========================================================

Lets start with the word:

What its the process in OOP when a child class derrives all the features
and characters from it's parent class?

total attempts: 0
total correct guesses: 0
remaining lives: 5
+------------------------------------------------------+
|                                                      |
|          I __ __ __ R __ __ __ N __ E                |
|                                                      |
+------------------------------------------------------+

```

After showing the word above, the user should now be able to select the position and add the word at the position.

example output:

```
===========================================================

total attempts: 0
total correct guesses: 0
remaining lives: 5
+------------------------------------------------------+
|                                                      |
|          I __ __ __ R __ __ __ N __ E                |
|                                                      |
+------------------------------------------------------+

select the position to insert the letter: 3

+------------------------------------------------------+
|                                                      |
|          I __ __ __ R __ __ __ N __ E                |
|                  /\                                  |
+------------------------------------------------------+

please insert the letter: E
Amazing!! you got a right answer

===========================================================

total attempts: 1
total correct guesses: 1
remaining lives: 5
+------------------------------------------------------+
|                                                      |
|          I __ __ E  R __ __ __ N __ E                |
|                                                      |
+------------------------------------------------------+
select the position to insert the letter: 1

+------------------------------------------------------+
|                                                      |
|          I __ __ E  R __ __ __ N __ E                |
|            /\                                        |
+------------------------------------------------------+
please insert the letter: M
Oops!! that's not right answer

===========================================================
total attempts: 2
total correct guesses: 1
remaining lives: 4
+------------------------------------------------------+
|                                                      |
|          I __ __ E  R __ __ __ N __ E                |
|                                                      |
+------------------------------------------------------+
select the position to insert the letter:
```

Once all the guesses are correct, the program should show the message saying you won.


create a dictionary to save all the words and it's definition in the following format:

```python
words = {
    "computer": "A machine that performs processes, calculations and operations based on instructions provided",
    "programming": "A set of instructions fed into the computer that performs particular computation",
    ...
}
```

create a class called `Game` that can store states of the game.
the states are as follows
- `current_word`
- `wrong_count`
- `list_of_guesses`
- add other required states / attributes if needed

The class `Game` can show the specific screen by calling different methods
- `create_guess_lists(self, word)`: creates a list eg: `['A', '_', '_', 'L', 'E']` out of `Apple`
- `generate_word_graphics(self, guesses, index)`: creates the box to display words

  **Example:**
  ```
    total attempts: 2
    total correct guesses: 1
    remaining lives: 4
    +------------------------------------------------------+
    |                                                      |
    |          I __ __ E  R __ __ __ N __ E                |
    |                                                      |
    +------------------------------------------------------+
  ```
    if the index value is given, it should be able to display the graphics of arrow ^ just below the blank space
- add other required methods / functions if needed


**Note:** *The instruction given above is for the reference only. You can create your own interface for the game*
