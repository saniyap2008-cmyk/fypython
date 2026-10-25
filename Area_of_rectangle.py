x = int(input("Enter the length: "))
y = int(input("Enter the breadth: "))
area = x * y
perimeter = 2 * (x + y)
if area<0:
 print("Please do not input negative values")
else:
 print (f"The area of the reactangle is: {area}")
