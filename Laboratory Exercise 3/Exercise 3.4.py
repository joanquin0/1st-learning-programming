#Exercise 3.4
import math
"""
This is a program that  takes the radius of a sphere (a floating-point number)
as input and then outputs the sphere’s diameter, circumference, surface area,
and volume.
"""

#Asks for the radius of a sphere in a floating point number
sphere_Radius = float(input("Enter the radius of a sphere: "))

#calculates for the diameter of the sphere
sphere_Diameter = sphere_Radius * 2
print("Diameter:\t", sphere_Diameter) #prints the diameter

#calculates for the circumference of the sphere
sphere_Circumference = 2 * math.pi * sphere_Radius
print("Circumference:\t", sphere_Circumference) #prints the circumference

#calculates for the surface area of the sphere
sphere_SurfaceArea = 4 * math.pi * (sphere_Radius ** 2)
print("Surface Area:\t", sphere_SurfaceArea) #prints the surface area

#calculates for the volume of the sphere
sphere_Volume = (4/3) * math.pi * (sphere_Radius ** 3)
print("Volume:\t\t", sphere_Volume) #prints the volume



