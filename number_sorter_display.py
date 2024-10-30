#Create a program that ask user to input a number ranging from 1 to 50.
print()
print("input number 1 - 50")
print()

try:
    var1 = int(input("Please input number here "))
except:
    print("Error try again")    
# Ask the user to input again until the user input is invalid.
# When the user input is invalid,
# display how many inputted numbers are in the following range: