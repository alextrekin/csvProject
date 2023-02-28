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
            max_line=0 # переменная для получения макисильного списка в словаре
            for i in reader:# проходим весь словарь чтобы получить самое большое значение
                line[j] = [i]
                j+= 1
                count = 0
                for elem in i:# делаем обход для вывода колонки
                    if (count) == rows:
                        print(elem,end='\n')
                    count+=1

    def search (self, Filename, search_item, change_item):
        pass