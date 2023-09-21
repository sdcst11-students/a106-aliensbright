#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254
import math
print("Today, I will find the volume of a sphere.")
radius = input("What is the radius of the sphere in meters?\n")
radius = float(radius)
volume = (4 * math.pi * radius ** 3) / 3 
print(f"The exact volume is {volume}m^3")
volume = round(volume , 2)
print(f"The appoximate volume is {volume}m^3")