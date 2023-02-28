import csv
class crud_master():
    def Reader_line(self, Filename, lines):
        with open(Filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            line = []
            lines -=1
            for i in reader:
                line.append(i)
            print(line[lines])

    def Reader_row(self, Filename, rows):
        with open(Filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            line = {} # создаем копию словаря для обхода
            rows -=1 #  уменьшаем на 1 потому что первый элемент ключа 0
            j=0 # переменная для прохода по ключу
            for i in reader:# проходим весь словарь чтобы получить самое большое значение
                line[j] = [i]
                j+= 1
                count = 0
                for elem in i:# делаем обход для вывода колонки
                    if (count) == rows:
                        print(elem,end='\n')
                    count+=1

    def search (self, Filename, search_item):
        with open(Filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            line = {}  # создаем копию словаря для обхода
            lines = 0
            j = 0  # переменная для прохода по ключу
            count = 0 #  сколко было найдено совпадений
            search_pos = [] #для того чтобы потом написать где нашел
            for i in reader:  # проходим весь словарь чтобы получить самое большое значение
                line[j] = [i]
                lines += 1
                rows = 0 #  считаем номер строки и столбца
                for elem in i:# делаем обход для вывода колонки
                    rows+=1
                    if (search_item) == elem:
                        pos = [lines,rows]
                        search_pos.append(pos)
                        count+=1
            if count>0:
                print(f'Значение {search_item}, было найдено {count} раз\nCтрока\tСтоблец')
                for elem in search_pos:
                    i = True
                    while i is True:
                        print(f"  {elem[0]} \t {elem[1]}\n")
                        i =False
            else:
                print('Значение не найдено')


