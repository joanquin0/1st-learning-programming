number = input("Enter number: ")
dist = int(input("Enter distance: "))
for ch in number:
    ov = ord(ch)
    decimal = ov - dist
    if decimal > 1:
        decimal_1= bin(decimal)[2:]
        decimal_2 = decimal_1[1:] + decimal_1[0]
    print("\nDecimal: ", decimal, "\nBinary: ", decimal_1, "\nResult: ", decimal_2)
