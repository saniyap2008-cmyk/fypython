day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
vd = [1, 3, 5, 7, 8, 10, 12]
vd2 = [4, 6, 9, 11]
leap = (year - 1584) % 4

if month == month<=12:
    print("Valid Month and Year")
else:
    print("Invalid Month.")
if month in vd and day <= 31:
    print("Valid Day and Year.")
elif month in vd2 and day <= 30:
    print("Valid Day. " \
        "Valid Year.")
elif month == 2 and day<= 28:
    print("Valid Day.")
elif leap == 0 and  month == 2 and day<=29:
      print("Valid Day and Year.")

else: 
    print("Invalid Day but valid Year.")




    
    