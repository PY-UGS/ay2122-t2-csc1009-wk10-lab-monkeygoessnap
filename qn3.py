# Create another Python project, 
# repeat the Question 2b and 2c from Laboratory Wk01

class Module:
    def __init__(self, arg):
        self.module = arg
        self.moduleName = {
            "CSC1006":"Mathematics 2",
            "CSC1007":"Operating Systems",
            "CSC1008":"Data Structures and Algorithms",
            "CSC1009":"Object-Oriented Programming",
            "CSC1010":"Computing Networks"
        }
    def printModuleName(self):
        try:
            print(self.moduleName[self.module])
        except:
            print("Unknown Module")


def main():
    m = Module("CSC10029")
    m.printModuleName()

if __name__ == '__main__':
    main()

