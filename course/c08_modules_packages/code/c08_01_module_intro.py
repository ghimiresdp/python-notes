"""
importing the whole module

"""
# import animal

# importing the individual element

from animal import DomesticAnimal

# we can also import multiple elements in the single line using commaa
from animal import Animal, DomesticAnimal

# we can also use small brackets so that we can import in different lines

from animal import (
    Animal,
    DomesticAnimal,
    WILD,
    DOMESTIC,
    abc,
)

abc()
elephant = Animal("John", "trumpet")

# elephant.name = "sdsds"
# elephant.paws = 34
# elephant.word = "sds"
elephant.speak()
elephant.rename("Jane")
elephant.speak()

cow = DomesticAnimal("My Cow", "moo")

print(DOMESTIC)
print(WILD)
