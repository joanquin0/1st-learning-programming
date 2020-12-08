#Exercise 3.10

"""
 This is a program that takes as inputs the hourly wage,
 total regular hours, and total overtime hours and displays an
 employee’s total weekly pay.
"""

#Asks for the hourly wage, total regular hours, and total overtime hours
hourly_wage = float(input("Enter hourly wage: "))
total_reg_hours = int(input("Enter total regular hours: "))
total_overtime = int(input("Enter totla overtime hours: "))
overtime_pay = total_overtime * (1.5 * hourly_wage)

#calculates the employee's total weekly pay
weekly_pay = (hourly_wage * total_reg_hours) + overtime_pay

#prints the weekly_pay
print("Employee's total weekly pay: Php", weekly_pay)
