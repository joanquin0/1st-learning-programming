max_distance = 26

def encrypt_or_decrypt():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        encrypt_decrypt = input().lower()
        if encrypt_decrypt in 'encrypt e decrypt d'.split():
            return encrypt_decrypt
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def message():
    print('Enter your message:')
    return input()


def get_distance():
    distance = 0
    while True:
        print('Enter the distance number (1-%s)' % (max_distance))
        distance = int(input())
        if (distance >= 1 and distance <= max_distance):
            return distance


def translated_message(encrypt_decrypt, message, distance):
    if encrypt_decrypt[0] == 'd':
        distance = -distance
    translated = ''
    for i in message:
        if i.isalpha():
            num = ord(i)
            num += distance
            if i.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif i.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += i
    return translated


encrypt_decrypt = encrypt_or_decrypt()
message = message()
distance = get_distance()
print('Your translated text is:')
print(translated_message(encrypt_decrypt, message, distance))