import sys
import os

def check_delim(str):
    if str[0].rstrip()!=str[0] or str[1].lstrip()!=str[1]:
        return True
    else:
        return False
class Research():
    def __init__(self,path):
        self.path=path
    def check_the_file(self):
        with open(self.path,'r') as file:
                lines = file.readlines()
                if len(lines)<2:
                    raise ValueError("File must contain at least two lines: header and data.")
                header =lines[0].split(",")
                if len(header)!=2:
                    raise ValueError("Header have wrong format.")
                if check_delim(header):
                    raise ValueError("Header have wrong delimiter.")
                for line in lines[1:]:
                    data=line.split(",")
                    if len(data) !=2:
                        raise ValueError("Each data line must contain only two values")
                    if check_delim(data):
                        raise ValueError("Data have wrong delimiter.")

                    
                    if int(data[0]) not in [0,1] or int(data[1]) not in [0,1]:
                        raise ValueError("Data values must be 0 or 1.")
    def file_reader(self):
        if (os.path.exists(self.path)):
            self.check_the_file()
            with open(self.path,'r') as file:
                return file.read()
        else:
            raise ValueError("No such file or directory")
    

def main():
    print(Research(sys.argv[1]).file_reader(), end="")
if __name__ == '__main__':
    main()