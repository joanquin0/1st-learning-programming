#Joangumban A121
#IT101-2P.A121.3T.19.20 .Computer Programming Concepts 2 (Paired)
#Tuesday 19,2020
#1Define a shape class with a constructor that gives value to width(base), length(height). Define two subclasses triangle and rectangle that calculate the area of the shape. In the main method, define two variables a triangle and a rectangle and then calls the area() function using this two variables.
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width


newRectangle = Rectangle(22, 33)
print(newRectangle.rectangle_area())
#This code is to find the area of rectangle and to multiply the length by the width of rectangle and calculate the area of the rectangle . by the formula of Area=lw
b = int(input("Triangle area base : "))
h = int(input("Triangle area height : "))
#-This code is to find the base and height of a tringle  and compute the area using the formula of Area=h(b/2)
area = b * h / 2

print("area = ", area)









#2.Define a Bank Account class with a constructor that initializes value of balance to zero. Define two methods in this class namely withdraw and deposit. Each method has parameter amount.  Withdraw method subtracts amount from balance and returns its difference. Deposit adds amount to the existing balance and returns a new balance.
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print(" Bank Account A121")
#this code declaring that 0 balance using self-argument and I simplify a stamen welcome text. In function deposit and withdraw , amount is taken as input(in float) and is then added/subtracted to the balance.
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
#-this code Use an if condition to check whether there is a sufficientamount of money available in the account to process a fund withdrawal.

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)
#-this code  use a display function to display the remaining balance in the account. Then i create a object and call it to get the program executed
s = Bank_Account()

s.deposit()
s.withdraw()
s.display()





#3.Create a class named Circle with a constructor that gives value to radius. Define three methods which will compute the area, diameter and perimeter of a circle.
PI = 3.14
radius = float(input(' Please Enter the radius of a circle'))
diameter = 2 *radius
circumference =2 * PI * radius
area = PI * radius * radius
#-This code to radius of a circle 3.14 to defined as ratio of a circle of circumference and diameter.
print("\nArea is computed as =%.2f"%area)
print("Circumference is computed as= %.2f"%circumference)
print("Diameter is computed as= %.2f"%diameter)
#-This code is to compute area and circumference and diameter using this formula:
#Area is computed as A=(pi)(r)2
#Circumference is computed as C=2(pi)(r)
#Diameter is computed as D=2r
