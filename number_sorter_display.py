#Create a program that ask user to input a number ranging from 1 to 50.
print()
print("input number 1 - 50")
print()

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []

while True:
    try:
        var1 = int(input("Please input number  "))
        
        if 1 <= var1 <= 10:
               data1.append(var1)
        elif 11 <= var1 <= 20:
               data2.append(var1)
        elif 21 <= var1 <= 30:
               data3.append(var1)
        elif 31 <= var1 <= 40:
               data4.append(var1)
        elif 41 <= var1 <= 50:
               data5.append(var1)
        else:
            print("----------------------------------------")
            print("invalid number") 
            print("----------------------------------------")
            print("count 1 - 10", data1)
            print("count 11 - 20", data2)
            print("count 21 - 30", data3)
            print("count 31 - 40", data4)
            print("count 41 - 50", data5)
            print("----------------------------------------")
            
            break
        
    except:
        print("Error try again") 
        
# Ask the user to input again until the user input is invalid.
while True:
   var1 = (input("Add another number? "))
   if var1 == 'yes' or var1 == 'Yes' or var1 == 'Y' or var1 == 'y':
    while True:   
        try:
            var2 = int(input("Please input number "))
            
            if 1 <= var2 <= 10:
               data1.append(var2)
            elif 11 <= var2 <= 20:
               data2.append(var2)
            elif 21 <= var2 <= 30:
               data3.append(var2)
            elif 31 <= var2 <= 40:
               data4.append(var2)
            elif 41 <= var2 <= 50:
               data5.append(var2)
            else:
                print("----------------------------------------")
                print("invalid number") 
                print("----------------------------------------")
                print("count 1 - 10", data1)
                print("count 11 - 20", data2)
                print("count 21 - 30", data3)
                print("count 31 - 40", data4)
                print("count 41 - 50", data5)
                print("----------------------------------------")
                
                break
        
        except:
            print("Error try again")
           
        
# When the user input is invalid, display how many inputted numbers are in the following range:            
   else:
        print("----------------------------------------")
        print()
        print("thank you")
        print()
        print("count 1 - 10", data1)
        print("count 11 - 20", data2)
        print("count 21 - 30", data3)
        print("count 31 - 40", data4)
        print("count 41 - 50", data5)
        print("----------------------------------------")
        break
            
  
       

