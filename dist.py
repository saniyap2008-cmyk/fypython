import math
x1 = int(input("Enter the value of x1 co ordinate: "))
x2 = int(input("Enter the value of x2 co ordinate: "))
y1 = int(input("Enter the value of y1 co ordinate: "))
y2 = int(input("Enter the value of y2 co ordinate: "))
dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f"The distance between two points is:{dist}")