import csv, pandas
class crud_master():
    def Reader(self, Filename, lines):
        with open(Filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = lines
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(row)
                    line_count += 1
            print(f'Processed {line_count} lines.')
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