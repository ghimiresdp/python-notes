class AgeError(Exception):
    min_age = 0
    max_age = 100

    def __init__(self, age, *args):
        super().__init__(*args)
        self.age = age
    
    def __str__(self):
        return f'The age {self.age} is not in between {self.min_age} and {self.max_age}'

x = 101
if not x <=0 <=100:
    raise AgeError(x)

# AgeError: The age 101 is not in between 0 and 100
print(x)