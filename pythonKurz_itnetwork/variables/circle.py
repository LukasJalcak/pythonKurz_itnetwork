#My solution:

from math import pi

number = float(input("\nEnter the radius of the circle (cm): "))
print("\nThe circumference of the circle is:", (2 * pi) * number, "cm")
print("The area of the circle is:", pi * number ** 2, "cm^2")
input("\nTo exit the program, press: ENTER")

#Solution from itnetwork.cz:
"""
r = float(input("Enter the radius of the circle (cm): "))
o = 2 * 3.14 * r
s = 3.14 * r * r
print("The circumference of the circle is:", o, "cm")
print("The area of the circle is", s, "cm^2")
input()
"""