'''
                                                KEY MUST BE INT BETWEEN 1 AND 255
'''

def encrypt(file, key):
    with open(file, 'rb') as f: # rb = read by byte
        data = f.read()
    
    data = bytearray(data)
    for index, value in enumerate(data): # enumerate bthawel el list l index w value
        data[index] = value ^ key # ^ = XOR

    with open('AMT-' + file, 'wb') as f: # wb = write by byte
        f.write(data)


def decrypt(file, key):
    with open(file, 'rb') as f: # rb = read by byte
        data = f.read()
    
    data = bytearray(data)
    for index, value in enumerate(data): # enumerate bthawel el list l index w value
        data[index] = value ^ key # ^ = XOR

    with open('ANTI-' + file, 'wb') as f: # wb = write by byte
        f.write(data)


key = int(input('Enter key - '))
# ektb el file bl extension
file = input('file - ')
option = int(input('enter 1 to encrypt or 2 to decrypt -'))
if option == 1:
    encrypt(file, key)
elif option == 2:
    decrypt(file, key)
else:
    print('enta ghabi yala ma olna ya 1 ya 2 3id mn el awl b2a')