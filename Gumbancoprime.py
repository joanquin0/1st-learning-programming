
from math import gcd as gcd

first = int(input("Enter first int:"))
sec = int(input("Enter second int:"))

if gcd(first, sec) == 1:
    print(first, "and", sec, "These are coprime")
else:
    print(first, "and",  sec, "These are not coprime")

