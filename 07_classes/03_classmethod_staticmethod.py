# © https://sudipghimire.com.np
# %%
"""
# Methods, Class Methods and static methods


"""


# %%
class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

    @classmethod
    def get_legs(cls):
        return cls.legs

    @classmethod
    def init_human(cls):
        cls.legs = 2

    @staticmethod
    def age(date_of_birth):
        print(f"you're {2021 - date_of_birth} years old")


# %%
john = Animal('John')
john.legs = 2

print(john.legs)
print(john.get_legs())
john.age(1990)


# %%
class Length:
    @staticmethod
    def meter_to_cm(meter):
        print(Mass.kg_to_gram(5))
        return meter * 100


print(Length.meter_to_cm(5))


class Mass:
    @staticmethod
    def kg_to_gram(kg):
        x = 5  # meters
        # l = Length()
        # x = l.meter_to_cm(x)
        return kg * 1000


class Volume:
    @staticmethod
    def cubic(kg):
        return kg * 1000
