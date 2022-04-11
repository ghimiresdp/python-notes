from utils import clear_screen, display_message


class Student:
    def __init__(self) -> None:
        pass

    def show_menu(self):
        print('Student Management Screen')


class Grade:
    message = ''
    def __init__(self, name) -> None:
        self.name = name

    def _rename(self):
        self.message='This feature is unimplemented'

    def _list_students(self):
        self.message='This feature is unimplemented'

    def _add_student(self):
        self.message='This feature is unimplemented'

    def _remove_student(self):
        self.message='This feature is unimplemented'


    def _modify_student(self):
        self.message='This feature is unimplemented'

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
            '0':{
                'title': 'Go to Previous Menu'
            }
        }
        clear_screen()
        while True:
            clear_screen()
            print(f'[ Managing class {self.name} ]'.center(80,'='))
            for k, v in menu_items.items():
                print(f'{k}: {v["title"]}')
            if self.message.__len__() > 0:
                display_message(self.message)
            try:
                option = input("Please select an option: ")
                if option=='0':
                    return
                menu_items[option]['action']()

            except KeyError:
                self.message = "Option not available"
