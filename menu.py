import csv_work
from sys import platform
from os import system
class checker():

    def clear (self): # метод для проверки операционной системы и дальнейшей очистки экрана
    # for windows
        if platform == "linux" or platform == "linux2":
            system('clear')
    # for mac and linux(here, os.name is 'posix')
        else:
            system('cls')


    def __init__(self, Filename):
        liner = "Выберите строку"
        collumner = "Выберите столбец"
        searcher = "Найти значение"
        settinger = "Заменить значение"
        prog_exit = "Выход из программы"
        variateble = {1: liner, 2: collumner, 3: searcher, 4: settinger, 5: prog_exit}

        cycle = True
        while cycle is True:
            checker.clear(self)
            for Item in variateble.items():
                print(Item, end="\n")
            try:
                Selected = int(input("Введите цифру нужного вам пункта:"))
                if Selected in range(1, 6):
                    if Selected == 1:# вывод строки
                        lines = int(input("Введите строку для вывода:"))
                        csv_work.crud_master.Reader_line(self, Filename, lines)
                        input("Нажмите для продолжения...")
                    elif Selected == 2: # Вывод столбца
                        rows = int(input("Введите колонку для вывода:"))
                        csv_work.crud_master.Reader_row(self, Filename, rows)
                        input("Нажмите для продолжения...")
                    elif Selected == 3: # поиск
                        search_item = input("Введите что найти:")
                        csv_work.crud_master.search(self, Filename, search_item)
                        input("Нажмите для продолжения...")
                    elif Selected == 4:# замена
                        print("poka delayu")
                    elif Selected == 5: # выход из программы
                        print("Ну и иди нахуй")
                        cycle = False
                else:
                    print("Введите нужную цифру")
            except ValueError:
                print("Введите цифру")