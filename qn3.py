# Create another Python project, 
# repeat the Question 2b and 2c from Laboratory Wk01

# Program output (Question 2b):
# Object-Oriented Programming

# Program output (Question 2c):
# value of x :  101
# value of x :  99
# value of x :  97
# value of x :  95
# value of x :  93
# value of x :  91
# value of x :  89
# value of x :  87
# value of x :  85
# value of x :  83
# value of x :  81
# value of x :  79
# value of x :  77
# value of x :  75
# value of x :  73
# value of x :  71
# value of x :  69
# value of x :  67

# module class
class Module:
    # constructor
    def __init__(self, arg):
        # assign arg to self.module
        self.module = arg
        # define map of modulecode:modulename to reference
        self.moduleName = {
            "CSC1006":"Mathematics 2",
            "CSC1007":"Operating Systems",
            "CSC1008":"Data Structures and Algorithms",
            "CSC1009":"Object-Oriented Programming",
            "CSC1010":"Computing Networks"
        }
    # method to print module name    
    def printModuleName(self):
        # try to access map for module code
        try:
            print(self.moduleName[self.module])
        # if not print unknown module
        except:
            print("Unknown Module")

# def loop to print out odd number in descending order starting from 102 and ending with 66

def printOddLoop():
    for x in range(102, 65, -1):
        if x % 2 == 1:
            print("value of x : ", x)

# define main method
def main():
    #qn2b of lab wk01
    # initiate object
    m = Module("CSC1009")
    #call method to print module name
    m.printModuleName()

    #qn2b of lab wk01
    printOddLoop()
    
# check name and run main
if __name__ == '__main__':
    main()

