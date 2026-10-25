percentage = int(input("Enter your total percentage: "))
if percentage>=75:
    print("Distinction.")
elif percentage>= 65:
    print("First Class.")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Pass Class")
else:
    print("Failed.")