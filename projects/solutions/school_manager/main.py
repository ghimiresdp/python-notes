import shutil
from traceback import print_last
from turtle import clear
from typing import List
from school import ClassRoom
from utils import RECORD_PATH, clear_screen, display_message
import os
import json

class SchoolManager:
    message = ''
    def __init__(self) -> None:
        self.__classes: List[ClassRoom] = []
        if os.path.exists(RECORD_PATH):
            for file_path in os.listdir(RECORD_PATH):
                if file_path.endswith('.json'):
                    with open(f"{RECORD_PATH}/{file_path}", 'r', encoding='utf-8') as file:
                        class_data = json.load(file)
                    class_room = ClassRoom(class_data['name'])
                    class_room.load_record(class_data['students'])
                    self.__classes.append(class_room)
        else:
            os.mkdir(RECORD_PATH)


    def __create_class(self):
        self.message = ''
        name = input("Enter class Name: ")
        if name in [c.name for c in self.__classes]:
            self.message=f"The class with name {name} already exists"
            return
        self.__classes.append(ClassRoom(name))
        self.message= f"Class {name} successfully created"

    def __manage_class(self):
        while True:
            clear_screen()
            print('[ Select class to manage ]'.center(80, '='))
            for idx, cls in enumerate(self.__classes):
                print(f'{idx+1}: {cls.name}')
            print('0: Back to main menu')
            if self.message.__len__() > 0:
                display_message(self.message)
            try:
                option = int(input("\nPlease select an option: "))
                if option == 0:
                    self.message = ''
                    return
                self.__classes[option-1].show_menu()
            except (ValueError, IndexError):
                self.message ='Invalid option supplied'


    def show_menu(self):
        menu_items = {
            '1': {
                'title': 'Create a class',
                'action': self.__create_class
            },
            '2': {
                'title': 'Manage a class',
                'action': self.__manage_class
            },
            '0': {
                'title': 'Quit application',
            },
        }
        while True:
            clear_screen()
            print('[ School Management System ]'.center(80,'='))
            for k, v in menu_items.items():
                print(f'{k}: {v["title"]}')
            if self.message.__len__()>0:
                display_message(self.message)
            try:
                option = input("\nPlease select an option: ")

                if option=='0':
                    display_message("Good bye!!")
                    return
                menu_items[option]['action']()

            except KeyError:
                self.message = "Option not available"


if __name__ == '__main__':
    sm = SchoolManager()
    sm.show_menu()
