name = input("Enter last name:")
hourly_wage = float(input("Enter hourly wage:"))
hours_worked = float(input("Enter hours worked"))
date = input("Enter date in mm/dd/yy format:")
wage = hourly_wage * hours_worked

lname = "LAST_NAME"
hwage = "HOURLY_WAGE"
hworked = "HOURS_WORKED"
wg = "WAGE"
dt = "DATE"

x = ("%-15s %-15s %-15s %-15s %s" %(lname, hwage, hworked, wg, dt)) + '\n' + ("%-15s %-15s %-15s %-15s %s" %(name, hourly_wage, hours_worked, wage, date))

cr = open("payslip.txt", "a")
cr.write(x)
cr.close()

print("%-15s %-15s %-15s %-15s %s" %(lname, hwage, hworked, wg, dt))
print("%-15s %-15s %-15s %-15s %s" %(name, hourly_wage, hours_worked, wage, date))
