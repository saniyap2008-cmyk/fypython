import math
ui = int(input("Enter the weight in grams: "))
ex = ui / 1000
decimal = math.ceil((float(ex) - int(ex)) * 1000)
if ex == int:
    print(f"{ex} kilogram(s) and 0 grams")
else:
    print(f"{int(ex)} kilograms and {decimal} grams.")
