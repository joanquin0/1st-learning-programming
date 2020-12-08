

Salary = int(input("Enter salary:"))
yrs = int(input("Enter years:"))
interest = int(input("Enter interest:"))

print("Salary:", "Years:")
for i in range(yrs):
    a = salary*(inter/100)
    salary = round(salary + a, 2)
    print(salary, yrs)
