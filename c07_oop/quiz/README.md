# Chapter 7 OOP Quiz

Please read the note carefully and try to solve the problem below:

## Quiz Q0701

Create a class named Person and add the following attributes and methods:

- **name** `str`:     Instance attribute
- **age** `int`:      Instance attribute
- **gender** `bool`:   Instance attribute
- **weight** `float`:   Class attribute
- `year_of_birth()`:
    Returns the year by subtracting the age from the current year.
- `get_pronouns()`:
    Returns list of `['he', 'his', 'him']` or ['she', 'her', 'hers'] by checking the gender

The initializer method should take parameters: `name`, `age`, and `gender`

## Quiz Q0702

Create a class Item with the following properties

- name: `str`
- rate: `float`
- quantity: `float`

Create a class Bill with the following properties

- customer_name: `str`
- items: `List[Item]`
- `count_items()`:
  - counts the total number of items in the bill
- `total()`:
  - finds out the total price of the items in the bill
  - returns the grand total as a floating point number
- `print_invoice()`:
  - prints out the bill in the format as shown below.

Example: we have items as follows:

- rice: `5 kg`              `$2.4` per Kg
- apple: `1 kg`            `$1.0` per Kg
- notebook: `3 items`       `$1.5` per item

```
+------------------------------------------------------------+
|                          ABC Shop                          |
|............................................................|
|  Order Invoice for: John Doe                               |
|............................................................|
|  SN  name                        rate  Quantity     total  |
|   1  rice                         2.4       5.0      12.0  |
|   2  apple                        1.0       1.0       1.0  |
|   3  notebook                     1.5       3.0       4.5  |
|............................................................|
|                               Grand Total          $ 17.5  |
|............................................................|
|              Thank you for visiting ABC Shop               |
+------------------------------------------------------------+
```

Guide for creating the table:

- Outer Borders should be created with '-', '+', and '|' characters
- inner borders should be created with '.' character
- total width of bill: 60 excluding borders
- Grand Total should have the width of the bill and should be justified right
- headers and footers should be justified center
- you can call function `print_item_row()` to print each item in the row.
  you can change the function itself to print in your own format.

hints:

```python
print('+', '-' * 60, '+', sep='')
print('|', 'ABC Shop'.center(60), '|', sep='')
print('|', '.' * 60, '|', sep='')
print('|', '  Order Invoice for: John Doe'.ljust(60), '|', sep='')
print('|', '.' * 60, '|', sep='')
```

Solution:

```python
# answer
def print_item_row(sn, name, rate, quantity):
    # add bill header here

    # add customer name here

    # titles for table
    print(f'|  {sn: 2d}  {name.ljust(22)}  {rate: 8.1f}  {quantity: 8.1f}  {rate*quantity: 8.1f}  |')

    # print all items in rows here

    # print grand total here

    # print footer here


class Item:
    pass  # your code here


class Bill:
    # attributes

    # methods

    def print_invoice(self):
        print(f"|  SN  {'name'.ljust(22)}  {'rate'.rjust(8)}  Quantity  {'total'.rjust(8)}  |")
        # your code here
```

## Quiz Q0703

Create a class Vehicle add some attributes and methods to it

- name
- brand
- wheels_count
- engine_type
- braking_system

Create a child class `HeavyVehicle` and inherit all the attributes from the parent class Vehicle
    - change the `wheels_count` from 4 to 6  in the initializer or accept the value while instantiating
    - add more instance attributes like `max_load`, `mileage`, etc.

Create a child class `Bike` and inherit all the attributes from the parent class Vehicle

- change the wheels_count from 4 to 2 in the initializer
- add setter or getter methods to add bike number, and owner name
- try adding property instead of setter or getter for passenger/ pillion attribute

create different instances of `Vehicle`, `HeavyVehicle`, and `Bike` and check whether each other are subclasses
and instances of different classes or not.
"""
