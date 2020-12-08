print("CAESAR CIPHER")
plaintext = input("Input text:")
distance = int(input("Input distance:"))
code = ""
for cipher in plaintext:
    ordVal = ord(cipher)
    cipherVal = ordVal + distance
    if cipherVal > ord('z'):
        cipherVal = ord('a') + distance -\
                    (ord('z') - ordVal + 1)
    code += chr(cipherVal)
print("Encrypted message of ", plaintext, ":", code)