def shiftLeft (bitstring):
    bitstring = bitstring[1:]+bitstring[0]
    return (bitstring)

bits = input ("Input string of bits: ")

leftShift = shiftLeft(bits)

print()
print(bits, "bitstring shifted to the left:" , leftShift)
print()

def shiftRight (bitstring):
    bitstring = bitstring[len(bitstring)-1] + bitstring[0:len(bitstring)-1]
    return (bitstring)

bits = input ("Input string of bits: ")

rightShift = shiftRight(bits)

print()
print(bits , "bitstring shifted to the right:" , rightShift)
print()