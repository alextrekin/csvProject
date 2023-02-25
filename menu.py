import csv_work
class checker():

    def __init__(self):
        liner = "Выберите строку"
        collumner = "Введите столбец"
        searcher = "Найти значение"
        settinger = "Заменить значение"
        prog_exit = "Выход из программы"
        variateble = {1: liner, 2: collumner, 3: searcher, 4: settinger, 5: prog_exit}
        for Item in variateble.items():
            print(Item,end="\n")
        try:
            while cycle is True:
                Selected = int(input("Введите цифру нужного вам пункта:"))
                if Selected not in range(1,5):
                    print("Введите нужную цифру")
                    cycle = False
        except ValueError:
            print("Введите цифру")
        return Selected


    def __str__(self):
        print("m2")

