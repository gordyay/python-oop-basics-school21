class Research():
    def file_reader(self):
        with open("../ex00/data.csv",'r') as file:
            return file.read()
    

def main():
    res = Research()
    print(res.file_reader(), end="")
if __name__ == '__main__':
    main()