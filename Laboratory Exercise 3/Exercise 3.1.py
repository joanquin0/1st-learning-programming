#Exercise 3.1

#Declare variables and their respective values
tax_rate = 0.20 
dependent_Deduction = 3000.0 #this is the amount of the deduction per dependent
standard_deduction = 10000.0
#Enter the gross income and store it to the variable named gross_Income
gross_Income = float(input("Enter the gross income: "))

#Enter the number of dependents and store it to the variable named dependent_Number
dependent_Number = int(input("Enter number of dependents: "))

#This computes the taxable income
taxable_Income = gross_Income - standard_deduction - (3000 * dependent_Number)

#This computes for the tax
tax = taxable_Income * tax_rate

#This prints the income tax
print("The income tax is $", round(tax, 2))
