message = input("Enter message: ")
code = ""
for i in message:
    i = ord(i)
    i += 1
    if i == 0:
        print(0)
    else:
        bstring = ""
        while i > 0:
            remainder = i % 2
            i = i // 2
            bstring += str(remainder)
    code += bstring
    code += " "

def shiftLeft(bitstrng):
    bitstrng = bitstrng[1:]+bitstrng[0]
    return (bitstrng)
leftShift = shiftLeft(code)

print("Encrypted message:" , leftShift)
