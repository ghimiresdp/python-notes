"""
© https://sudipghimire.com.np

Create 2 different classes Major and Subject

create an instance of Major and add different subjects to the 'subject' attribute as a set of subjects

Create another instance for Major and add subjects to the instance

add operator overloading to add different methods so that we can create another major.

Example we have majors science, commerce

if we call

new_major = science + commerce

it should be able to return the new instance of Major with all subjects inside of them

Note:
    you can try other operator overloading options too.
"""

# answer


class Subject:

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"subject: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()


class Major:
    name = ''

    def __init__(self, name) -> None:
        self.name = name
        self.subjects = []

    def __add__(self, other: "Major"):
        sub = Major(f'{self.name} + {other.name}')
        sub.subjects = [*self.subjects, *other.subjects]
        return sub


# Tests

sc = Major("Science")
sc.subjects.append(Subject('Physics'))
sc.subjects.append(Subject('Chemistry'))

com = Major("Commerce")
com.subjects.append(Subject('Business Mathematics'))
com.subjects.append(Subject('Accounting'))

new_major = sc + com

print(new_major.name)
print(new_major.subjects)
