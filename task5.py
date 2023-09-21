#! python3

# Test output Volume of 20.22 should give radius of:1.69002229118
#volume = 4/3 pi r^3
# r^3 = 3volume/4pi
import math
print("Today I will find the radius of a sphere.")
volume = float(input("What is the volume of the sphere in meters?>"))
radius = (3 * volume / (4 * math.pi))**1.0/3
print(f"The radius of the sphere is {radius} meters.")