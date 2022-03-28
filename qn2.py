# Create a new Python project, take user keyboard input for 2 numbers (x and y), then
# print out the average of these 2 numbers: (x + y)/2

# get input for x
x = input("input x: ")
# get input for y
y = input("input y: ")
# print average of the 2 numbers
# error checking incase string
try:
    # try cast to float
    output = (float(x) + float(y))/2
    # prints the average of the 2 number 
    # if casted successfully
    print("average of these 2 numbers is :", output)
# error handling
except:
    # prints invalid inputs incase of string entered
    print("invalid inputs")
