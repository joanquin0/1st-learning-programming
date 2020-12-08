class Employee:
    def __init__(self):
        self._salary=15000
    def income(self):
        print("Employee Net Salary is {}".format(self._salary))
    def setSalary(self,salary):
        self._salary=salary
c=Employee()
c.income()
c.salary=10000
c.income()
c.setSalary(10000)
c.income()
