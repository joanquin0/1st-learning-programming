#Exercise 3.3

"""
This program is to calculate the total cost of the rental fee of the customer
who rents a DVD
"""

#Variable Declaration on the Prices of the videos
newVideo_Price = 3.0
oldVideo_Price = 2.0

#Asks for the number of New Videos to be rented
new_Videos = int(input("Enter the quantity to be borrowed: "))

#Asks for the number of Old Videos to be rented
old_Videos = int(input("Enter the quantity to be borrowed: "))

#Calculates the total cost
totalCost = ((new_Videos * newVideo_Price) + (old_Videos * oldVideo_Price))
#prints the total cost of the rent
print("The total cost of the rental is Php", totalCost)
