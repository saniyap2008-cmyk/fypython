import random
print("To generate a random number please input limits.")
lp = int(input("Enter the lower limit: "))
up = int(input("Enter the upper limit: "))
number = random.randint(lp, up)
print(number)
