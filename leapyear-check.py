
print("To check for leap years: ")
year = int(input("Enter the year you want to check: "))
leap = (year - 1584) % 4
if leap == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")