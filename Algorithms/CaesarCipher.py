
# Encrypts or decrypts a message using the Ceasar Cipher
# Also has option to brute force an encoded message
# Utilizes ASCII integers (chr()) to represent the alphabet (ord()) and 26 keys


MAX_KEY_SIZE = 26

def getMode():
    while True:
        mode = input('Would you like to (e)ncrypt, (d)ecrypt or (b)rute force a message? > ').lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e", "decrypt" or "d", or "brute" or "b".')

print('This is a Caesar Cipher program for Cryptography.\n')

def getMessage():
    return input('What is your message? > ')

def getKey():
    key = int(input('Enter the key number (1-%s) > ' % MAX_KEY_SIZE))
    if (key >= 1 and key <= MAX_KEY_SIZE):
        return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:\n')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
        