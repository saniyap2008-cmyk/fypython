pa = int(input("Enter the principal amount: "))
time = float(input("Enter time (in years): "))
ir = float(input("Enter the annual interest rate in (%): "))
formula = (pa * time * ir) // 1000
if time>= 1:
 print(f"The simple interest for {time} years is {formula}. ")
elif time<= 1 and time>=0:
 print(f"The simple interest for {time} year is {formula}. ")
else:
 print("Incorrrect values provided.")