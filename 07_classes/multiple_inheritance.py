# %% Multiple Inheritance
class Shop:
    reg_no = 0


class CoffeeShop(Shop):
    coffee_price = 0


class Bakery(Shop):
    dough_nut_price = 0


class Restaurant(CoffeeShop, Bakery):
    pass


r1 = Restaurant()

r1.dough_nut_price = 10

print(r1.reg_no)
print(r1.dough_nut_price)
print(r1.coffee_price)

# %%

print(isinstance(r1, Restaurant))
print(isinstance(r1, Bakery))
print(isinstance(r1, CoffeeShop))
print(isinstance(r1, Shop))

###
"""
Prime Number

- if number is directly divisible by 1 or itself only,
 then it is prime number

- the number must be greater than 2

- we have to loop from 2 upto half of the number (integer division)
    - if any number does not give remainder it is composite

"""


