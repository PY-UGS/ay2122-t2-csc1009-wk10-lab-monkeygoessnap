# Question 2:
# Create a new Python project, take user keyboard input for 2 numbers (x and y), then
# print out the average of these 2 numbers: (x + y)/2

# Program output 1:
# input x: 10
# input y: 20
# average of these 2 numbers is : 15.0

# Program output 2 (Error checking):
# input x: b
# invalid inputs


# error checking incase string
try:
    # try cast to float
    output = (float(input("input x: ")) + float(input("input y: ")))/2
    # prints the average of the 2 number 
    # if casted successfully
    print("average of these 2 numbers is :", output)
# error handling
except:
    # prints invalid inputs incase of string entered
    print("invalid inputs")
