import encryptors
stop = False

print('''
    Welcome to Text Encryptor Encryption Algorithm!
    Type 'h' for help


''')
while stop == False:
    
    command = input('>')

    if command == 'h':
        print('''What do you want to do?
        1. Generate a new key - g
        2. Encrypt Text - e
        3. Decrypt Text - d
        4. Quit this app - q''')
    elif command == 'g':
        encryptors.generateKey()
    elif command == 'e':
        encryptors.encode()
    elif command == 'd':
        encryptors.decode()
    elif command == 'q':
        exit()
    else:
        print('Command not found.')