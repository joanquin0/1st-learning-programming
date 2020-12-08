#Exercise 3.6

"""
This is a program that accepts an object’s mass (in kilograms) and
velocity (in meters per second) as inputs and then outputs its momentum.
This program also calculates for the kinetic energy of the object
"""

#Asks for the object's mass in Kilogram
object_Mass = float(input("Enter mass in Kilogram: "))

#Asks for the velocity in meters per second
velocity = float(input("Enter velocity in meters per second: "))

#Calculates for the object's momentum
momentum = object_Mass * velocity

#Calculates for the object's kinetic energy
kinetic_Energy = (1/2) * object_Mass * (velocity ** 2)


#prints the momentum of the object
print("The momentum of the object is", momentum)
print("The kinetic energy is", kinetic_Energy)
