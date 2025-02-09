import os
from random import randint

def check_delim(str):
    if str[0].rstrip()!=str[0] or str[1].lstrip()!=str[1]:
        return True
    else:
        return False
class Research():
    def __init__(self,path):
        self.path=path
    def check_the_file(self, has_header = True):
        with open(self.path,'r') as file:
                lines = file.readlines()
                if has_header:
                    start = 1
                    if len(lines)<2:
                        raise ValueError("File must contain at least two lines: header and data.")
                    header =lines[0].split(",")
                    if len(header)!=2:
                        raise ValueError("Header have wrong format.")
                    if check_delim(header):
                        raise ValueError("Header have wrong delimiter.")
                else :
                    start = 0
                    if len(lines)<1:
                        raise ValueError("File must contain at least one line of data.")
                for line in lines[start:]:
                    data=line.split(",")
                    if len(data) !=2:
                        raise ValueError("Each data line must contain only two values")
                    if check_delim(data):
                        raise ValueError("Data have wrong delimiter.")
                    if int(data[0]) not in [0,1] or int(data[1]) not in [0,1]:
                        raise ValueError("Data values must be 0 or 1.")
                    if int(data[1]) + int(data[0]) != 1:
                        raise ValueError("Data values must be 0,1 or 1,0.")
    def file_reader(self, has_header = True):
        if has_header:
            start=1
        else:
            start = 0
        if (os.path.exists(self.path)):
            self.check_the_file(has_header)
            with open(self.path,'r') as file:
                lists = [[int(item) for item in line.strip().split(",")] for line in file.readlines()[start:]]
                return lists
        else:
            raise ValueError("No such file or directory")
    class Calculations():
        def __init__(self, data):
            self.data = data
        def counts(self,data):
            heads=0
            tails=0
            for line in data:
                heads+=line[0]
                tails+=line[1]
            return heads, tails
        def fractions(self):
            heads, tails = self.counts(self.data)
            sum = heads + tails
            if sum == 0:
                return 0, 0
            f1 = heads/sum * 100
            f2 = tails/sum * 100
            return f1, f2
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)

        def predict_random(self, num):
            predict = []
            for _ in range(num):
                prediction = randint(0, 1)
                if prediction == 0:
                    predict.append([0, 1])
                else:
                    predict.append([1, 0])
            return predict
        def predict_last(self):
            return self.data[-1]
        def save_file(self,data, name, format):
            with open(f"{name}.{format}", 'w') as export:
                export.write(data)
    
