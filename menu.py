# 
# Класс служит шаблоном для меню лаб.
# ver. 0.1 alpha
# Creater: Griffon
# 

class Menu: 
    def get_header(self, number=0,variant=0):
        print(f"""Лабораторная работа № {number}
Вариант работы: {variant}
Создатель программы: Griff""")
        self.get_line(20)

    def get_helplist(self,commands): # Принимает словарь команд 
        print("Список команд")
        self.get_line(20)
        for key in commands:
            print(key, commands[key])

    def get_line(self, size = 5):
        print("-" * size)
    
    def get_com_keys(self, commands):
        com_list = list()

        for key in commands:
            com_list.append(key)

        return(com_list)
        # print(com_list)

