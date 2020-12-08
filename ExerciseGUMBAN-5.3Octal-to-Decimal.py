# Python Program - Convert Octal to Decimal

print("Enter 'x' for exit.");
octal = input("Enter number in Octal Format: ");
if octal == 'x':
    exit();
else:
    decimal = str(int(octal, 8));
    print(octal,"in Decimal =",decimal);