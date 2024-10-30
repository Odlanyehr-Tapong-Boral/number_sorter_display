#Create a program that ask user to input a number ranging from 1 to 50.
print()
print("input number 1 - 50")
print()

while True:
    try:
        var1 = int(input("Please input number  "))
        break
    except:
        print("Error try again")    
# Ask the user to input again until the user input is invalid.
var2 = (input("Add another number? "))
if var2 == 'yes' or var2 == 'Yes' or var2 == 'Y' or var2 == 'y':

    while True:
        try:
            var3 = int(input("Please input number "))
            break
        except:
            print("Error try again")

# When the user input is invalid, display how many inputted numbers are in the following range: