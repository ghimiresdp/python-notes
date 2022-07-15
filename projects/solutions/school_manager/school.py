import json
from typing import List
from utils import clear_screen, display_message, RECORD_PATH


class Student:

    def __init__(self, name: str, roll: int, age: int, major: str) -> None:
        self.name = name
        self.roll = roll
        self.age = age
        self.major = major

    def show_menu(self):
        print('Student Management Screen')

    def modify(self) -> bool:
        clear_screen()
        changed = False
        print(f'[ Modifying "{self.name}" ]'.center(80, '='), end='\n\n')
        name = input(f"Enter New name [Enter to set {self.name}]")
        if name.__len__():
            self.name = name
            changed=True

        roll = input(f"Enter New name [Enter to set {self.roll}]")
        if roll.__len__():
            self.roll = int(roll)
            changed=True

        age = input(f"Enter New name [Enter to set {self.age}]")
        if age.__len__():
            self.age = int(age)
            changed=True

        major = input(f"Enter New name [Enter to set {self.major}]")
        if major.__len__():
            self.major = major
            changed=True
        return changed


class ClassRoom:
    message = ''

    def __init__(self, name) -> None:
        self.name = name
        self.__students: List[Student] = []

    def load_record(self, students: list):
        for std in students:
            self.__students.append(Student(**std))

    def save_record(self):
        with open(f"{RECORD_PATH}/{self.name}.json", 'w', encoding='utf-8') as file:
            json.dump({'name': self.name, 'students': [s.__dict__ for s in self.__students]}, file, indent=2)

    def _rename(self):
        self.message = 'This feature is unimplemented'

    def _list_students(self):
        clear_screen()
        print(f'[ Class "{self.name}" Student ]'.center(80, '='), end='\n\n')
        print('+', '-' * 6, '+', '-' * 32, '+', '-' * 5, '+', '-' * 17, '+', sep='')
        print(f"| {'Roll':4s} | {'Name'.center(30)} | {'Age':3s} | {'Major'.center(15)} |")
        print('+', '-' * 6, '+', '-' * 32, '+', '-' * 5, '+', '-' * 17, '+', sep='')
        for std in self.__students:
            print(f"| {std.roll:4d} | {std.name:30s} | {std.age:3d} | {std.major:15s} |")
        print('+', '-' * 6, '+', '-' * 32, '+', '-' * 5, '+', '-' * 17, '+', sep='')
        input("\nPress Enter to go back: ")

    def _add_student(self):
        self.message = ''
        clear_screen()
        print('[ Adding Student ]'.center(80, '='))
        try:
            std = Student(
                name=input("Enter Student name: "),
                roll=int(input("Enter Student roll: ")),
                age=int(input("Enter Student age: ")),
                major=input("Enter Student major: "),
            )
            self.__students.append(std)
            self.save_record()
            self.message = f'Student "{std.name}" successfully added'
        except ValueError:
            self.message = 'invalid data entered'

    def _remove_student(self):
        try:
            roll: int = int(input("Enter the roll number of a student to remove from the class: "))
            students_count = self.__students.__len__()
            self.__students = [s for s in self.__students if s.roll != roll]
            if students_count == self.__students.__len__():
                self.message = f'No student with roll "{roll}" found'
                return
            self.save_record()
            self.message = 'student successfully removed'
        except (ValueError, IndexError):
            self.message = 'Invalid Option Supplied'

    def _modify_student(self):
        try:
            roll: int = int(input("Enter the roll number of a student to modify: "))
            student = [s for s in self.__students if s.roll == roll][0]
            success = student.modify()
            if success:
                self.save_record()
                self.message = 'student successfully updated'
            else:
                self.message = "No Changes were made"
        except (ValueError, IndexError):
            self.message = 'Student not found'

    def show_menu(self):
        menu_items = {
            '1': {
                'title': 'Rename the class',
                'action': self._rename
            },
            '2': {
                'title': 'List Students',
                'action': self._list_students
            },
            '3': {
                'title': 'Add Student',
                'action': self._add_student
            },
            '4': {
                'title': 'Remove Student',
                'action': self._remove_student
            },
            '5': {
                'title': 'Modify Student',
                'action': self._modify_student
            },
            '0': {
                'title': 'Go to Previous Menu'
            }
        }
        clear_screen()
        self.message = ''
        while True:
            clear_screen()
            print(f'[ Managing class {self.name} ]'.center(80, '='))
            for k, v in menu_items.items():
                print(f'{k}: {v["title"]}')
            if self.message.__len__() > 0:
                display_message(self.message)
            try:
                option = input("\nPlease select an option: ")
                if option == '0':
                    return
                menu_items[option]['action']()

            except (KeyError, ValueError):
                self.message = "Invalid option supplied"
