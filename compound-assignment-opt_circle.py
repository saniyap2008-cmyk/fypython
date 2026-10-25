r = int(input("Enter the radius of the circle: "))
import math
area = math.pi
area *= r
area *= r
if area<0:
 print("Please do not input negative values")
else:
 print (f"The area of the circle is: {area}")