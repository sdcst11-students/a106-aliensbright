#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
print("Today I will solve the surface area of a cone.")
radius = float(input("What is the radius?>"))
height = float(input("What is the vertical height?>"))
slantH = ( radius**2 + height**2 )**0.5
print(f" The slant is {slantH}.")
SurfaceArea = math.pi * ( radius**2 + radius * slantH)
print(f"The surface area of a cone with radius {radius} and height {height} is {SurfaceArea}")
