
import beta
from menu import Menu
import os
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
menu=Menu()
commands = {
    "q": "Выход",
    "h": "Список команд",
    "enc": "Шифрование",
    "dec": "Дешифрование",
}

def choice_menu (com_list):
    while True:
        user_command = input("Введите команду:")

        if user_command == com_list[0]:
            # clear()
            exit()

        elif user_command == com_list[1]:
            # clear()
            menu.get_helplist(commands)

        elif user_command == com_list[2]:
            beta.enctyption()
            # clear()
           
        elif user_command == com_list[3]:
           beta.dectyption()
        
        elif user_command == com_list[4]:
            None
        
        elif user_command == com_list[5]:
            None

        elif user_command == "cls":
            clear()
            
        else:
            print("""Не верная команда
Для вывода списка команд введите 'h'""")
            
menu.get_header(6,8)
choice_menu(menu.get_com_keys(commands))
