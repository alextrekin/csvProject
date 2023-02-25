import csv

class crud():

    def __init__(self):
        print("1")

    def __str__(self):
        print("2")

    def Reader(Filename = ""):
        with open(Filename,"r",newline='\n') as csvfile:
            DataReader = csv.reader(
                csvfile,
                delimiter="\n",
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            Output = []
            for Item in DataReader:
                Output.append(Item[0])
            csvfile.close()
            print("Данные прочитаны!")
            return Output
        print("3")

    def Writer(self):
        print("4")

    def Getter(self):
        print("5")

    def Settter(self):
        print("6")