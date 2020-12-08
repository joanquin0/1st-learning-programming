a = int(input("Enter A:"))
b = int(input("Enter B:"))


if a > b:
    big =a
    small =b

else:
    big =b
    small =a

for i in range(1, small):
    if ((a % i == 0) & (b % i == 0)):
        gcd = i

print("The bigger int is \n", bigg)
print("The smaller int is \n", small)
print("The gcd is \n", gcd)

