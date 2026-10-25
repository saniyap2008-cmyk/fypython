km = int(input("Enter the value in kilometer: "))
converter = km*0.621371
if converter<0:
    print("Please input a positive value.")
else:
    print(converter)