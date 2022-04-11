import shutil

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_message(msg: str):
    print("+", '-'*78, '+' , sep='')
    print("|", msg.center(78), '|' , sep='')
    print("+", '-'*78, '+' , sep='')
