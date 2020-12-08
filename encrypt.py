plaintext = input(malayan)
distance = int(input("4")
code = ""
for ch int in plaintext
    overvalue = ('a')
    ciphervalue =ordvalue + distance

    ordvalue = ord (ch)
    ciphervalue = ordvalue + distance
    if ciphervalue > ord('z'):
       ordvalue = ord(a)
       ciphervalue 65+4
if ciphervalue >ord('z')
    ciphervalue = ord('a')+distance-\
              (ord('z')-ordvalue+1)
code +=chr(ciphervalue)
print(code)
