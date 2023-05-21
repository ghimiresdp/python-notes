"""
© https://sudipghimire.com.np

Create a class Employee that contains different attributes.
- id
- first_name
- last_name
- project
- department
- salary

Make attributes project, department, and salary as private and use getter and setter methods to get and
set respective values

id should be private and can only be initialized when employee instance is created

first_name and last_name should be initialized with constructor and can be changed any time
"""

# answer


class Employee:

    def __init__(self, id, first_name, last_name) -> None:
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name

        self.__project = ''
        self.__department = ''
        self.__salary = ''

    def get_project(self):
        return self.__project

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def set_project(self, project: str):
        self.__project = project

    def set_department(self, department: str):
        self.__department = department

    def set_salary(self, salary: int):
        self.__salary = salary


# Test
john = Employee(1, "John", "Doe")

john.set_project("ABC management system")

john.set_salary(5000)
john.set_department("Software")


print(john.get_department())
print(john.get_salary())
print(john.get_project())

john.last_name = "Lennon"

print(john.first_name, john.last_name)
