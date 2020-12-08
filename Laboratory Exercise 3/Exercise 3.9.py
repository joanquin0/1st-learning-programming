#Exercise 3.9

"""
 This is a program that takes as input a number of kilometers and prints the
 corresponding number of nautical miles.
"""

#Asks for the user for the distance in kilometers
distance_kilometer = float(input("Enter distance in kilometer: "))

"""
calculates the conversion of degrees and mins between the north pole and the
equater. 
"""
convert = 10000 / (90 * 60)
#calculates the nautical miles
nautical_miles = distance_kilometer / convert

#Prints the nautical miles
print("Nautical Miles:", nautical_miles)
