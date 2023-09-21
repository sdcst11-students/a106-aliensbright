#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# test case: 5, 1, 11 should give x = 2
print("Today I will solve your two step equation.")
a = float(input("What is \"a\" equal to?>"))
b = float(input("What is \"b\" equal to?>"))
c = float(input("What is \"c\" equal to?>"))
print(f"The equation is {a}x+{b}={c}")
x = (c-b)/a
print(f"x is equal to {x}.")
