print("                                                 Arithmetic Calculator program                                                     ")

num01 = int(input("Enter the first number: "))
num02 = int(input("Enter the second number (or power for exponential calculation): "))
opt = input("Enter the arithmetic operation: ")
add = num01 + num02
subtract = num01 - num02
multiply = num01 * num02
divide = num01 / num02
remainder = num01 % num02
floordivision = num01 // num02
expo = num01 ** num02
if opt == "add":
   print(add)
if opt == "subtract" :
   print(subtract)
if opt == "multiply":
   print(multiply)
if opt == "divide":
   print(divide)
elif opt == "floor division":
   print(floordivision)
elif opt == "Remainder":
   print(remainder)
elif opt == "Exponential" or "Square":
   print(expo)


else:
    if opt != "add" and "subtract" and "multiply" and "divide":
     print("Incorrect arithmetic operation")