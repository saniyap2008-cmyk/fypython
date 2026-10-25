print("To find the roots of the equation ax^2 + bx + c: ")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
import math
r1 = ((-b) + math.sqrt((b**2 - 4*a*c))) / 2 * a
r2 = ((-b) - math.sqrt((b**2 - 4*a*c))) / 2 * a
print(f"The roots are {r1} & {r2}.")

