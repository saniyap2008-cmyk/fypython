import math
force = 100
angle = math.radians(30)
vertical = math.cos(angle)
vertical_F = force * vertical
print(f"The vertical component is {vertical_F}")