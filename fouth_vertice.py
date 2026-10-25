print("To the value of the fourth vertex input the co ordinates: ")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))


M1x = (x3 - x2) / 2
M1y = (y3 - y2) / 2

x4 = (2 * M1x) + x1
y4 = (2 * M1y) + y1
print(f"The co ordinates of the fourth vertex is: {x4 , y4}")