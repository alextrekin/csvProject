import csv_work, os
class checker():

    def __init__(self, Filename):
        liner = "Выберите строку"
        collumner = "Введите столбец"
        searcher = "Найти значение"
        settinger = "Заменить значение"
        prog_exit = "Выход из программы"
        variateble = {1: liner, 2: collumner, 3: searcher, 4: settinger, 5: prog_exit}

        cycle = True
        while cycle is True:
            os.system('cls||clear')
            for Item in variateble.items():
                print(Item, end="\n")
            try:
                Selected = int(input("Введите цифру нужного вам пункта:"))
                if Selected in range(1, 6):
                    if Selected == 1:
                        lines = int(input("Введите строку для вывода:"))
                        csv_work.crud_master.Reader_line(self, Filename, lines)
                        input()
                    elif Selected == 2:
                        rows = int(input("Введите колонку для вывода:"))
                        csv_work.crud_master.Reader_row(self, Filename, rows)
                    elif Selected == 3:
                        csv_work.crud_master.Reader_row(self, Filename, search_item, change_item )
                    elif Selected == 4:# делаю сейчас поиск
                        print("poka delayu")
                    elif Selected == 5:
                        print("Ну и иди нахуй")
                        cycle = False
                else:
                    print("Ввкдите нужную цифру")
            except ValueError:
                print("Введите цифру")



    def __str__(self):
        print("m2")

