print("To calculate the maximum of three numbers: ")
num01 = int(input("Enter number 01: "))
num02 = int(input("Enter number 02: "))
num03 = int(input("Enter number 03: "))
if num01>num02 and num01>num03:
    print (f"{num01} is the greatest.")
elif num02>num01 and num02>num03:
    print(f"{num02} is the greatest.")
elif num03>num02 and num03>num01:
    print(f"{num03} is the greatest.")
else:
    print("Two or more numbers are equal.")
    #if -elif and else:
# if (Condition):
    #indented block to print
# elif (Condition):
    #indented block to print
# elif (Condition):
    #indented block to print
# else: 