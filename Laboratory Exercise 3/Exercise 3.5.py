#Exercise 3.5

"""
This is a program that accepts an object’s mass (in kilograms) and
velocity (in meters per second) as inputs and then outputs its momentum.
"""

#Asks for the object's mass in Kilogram
object_Mass = float(input("Enter mass in Kilogram: "))

#Asks for the velocity in meters per second
velocity = float(input("Enter velocity in meters per second: "))

#Calculates for the object's momentum
momentum = object_Mass * velocity

#prints the momentum of the object
print("The momentum of the object is", momentum)
