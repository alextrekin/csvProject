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
            row = []
            rows -=1
            for i in reader:
                row.append(i)
            print(row[rows])

class crud(crud_master):

    def __init__(self):
        pass

    def __str__(self):
        pass

    def Writer(self):
        pass

    def Getter(self):
        pass

    def Settter(self):
        pass