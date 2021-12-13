import random
import string

def generateKey():
    letters = string.ascii_lowercase 
    key = ''.join((random.sample(letters, 26)))   
    print(f'''
        This is your key: {key} 
        Copy it somewhere and keep it safe!
    ''')


def encode():
    print('''
    Welcome to the encryptor. Type in 'quit' to quit this function.
    Please note that this program will NOT work unless
    a valid key generated also by this program is entered

    ''')
    key = input('Please enter a key: ')
    if key == 'quit':
        return
    
    print('Thanks, now please enter any text you want to encrypt. Remember, typing quit will take you to the home page.')
    
    quit = False
    while quit == False:
        userInput = input(': ')
        if userInput == 'quit':
            quit = True
        else:
            keyArray = []
            encodedCharacters = []

            for char in key:
                keyArray.append(char)
            
            for letter in userInput:
                if letter == 'a':
                    encodedCharacters.append(keyArray[0])
                elif letter == 'b':
                    encodedCharacters.append(keyArray[1])
                elif letter == 'c':
                    encodedCharacters.append(keyArray[2])
                elif letter == 'd':
                    encodedCharacters.append(keyArray[3])
                elif letter == 'e':
                    encodedCharacters.append(keyArray[4])
                elif letter == 'f':
                    encodedCharacters.append(keyArray[5])
                elif letter == 'g':
                    encodedCharacters.append(keyArray[6])
                elif letter == 'h':
                    encodedCharacters.append(keyArray[7])
                elif letter == 'i':
                    encodedCharacters.append(keyArray[8])
                elif letter == 'j':
                    encodedCharacters.append(keyArray[9])
                elif letter == 'k':
                    encodedCharacters.append(keyArray[10])
                elif letter == 'l':
                    encodedCharacters.append(keyArray[11])
                elif letter == 'm':
                    encodedCharacters.append(keyArray[12])
                elif letter == 'n':
                    encodedCharacters.append(keyArray[13])
                elif letter == 'o':
                    encodedCharacters.append(keyArray[14])
                elif letter == 'p':
                    encodedCharacters.append(keyArray[15])
                elif letter == 'q':
                    encodedCharacters.append(keyArray[16])
                elif letter == 'r':
                    encodedCharacters.append(keyArray[17])
                elif letter == 's':
                    encodedCharacters.append(keyArray[18])
                elif letter == 't':
                    encodedCharacters.append(keyArray[19])
                elif letter == 'u':
                    encodedCharacters.append(keyArray[20])
                elif letter == 'v':
                    encodedCharacters.append(keyArray[21])
                elif letter == 'w':
                    encodedCharacters.append(keyArray[22])
                elif letter == 'x':
                    encodedCharacters.append(keyArray[23])
                elif letter == 'y':
                    encodedCharacters.append(keyArray[24])
                elif letter == 'z':
                    encodedCharacters.append(keyArray[25])
                elif letter == ' ':
                    encodedCharacters.append('#')
                else:
                    encodedCharacters.append(letter)

            encryptedString = ''.join(encodedCharacters)
            print(f'''Encrypted Text: {encryptedString}''')


def decode():
    print('''
    Welcome to the decryptor. Type in 'quit' to quit this function.
    Please note that this program will NOT work unless
    a valid key generated also by this program is entered

    ''')
    key = input('Please enter a key: ')
    if key == 'quit':
        return
    
    print('Thanks, now please enter any text you want to decrypt. Remember, typing quit will take you to the home page.')
    
    quit = False
    while quit == False:
        userInput = input(': ')
        if userInput == 'quit':
            quit = True
        else:
            keyArray = []
            decodedCharacters = []

            for char in key:
                keyArray.append(char)
            
            for letter in userInput:
                if letter == keyArray[0]:
                    decodedCharacters.append('a')
                elif letter == keyArray[1]:
                    decodedCharacters.append('b')
                elif letter == keyArray[2]:
                    decodedCharacters.append('c')
                elif letter == keyArray[3]:
                    decodedCharacters.append('d')
                elif letter == keyArray[4]:
                    decodedCharacters.append('e')
                elif letter == keyArray[5]:
                    decodedCharacters.append('f')
                elif letter == keyArray[6]:
                    decodedCharacters.append('g')
                elif letter == keyArray[7]:
                    decodedCharacters.append('h')
                elif letter == keyArray[8]:
                    decodedCharacters.append('i')
                elif letter == keyArray[9]:
                    decodedCharacters.append('j')
                elif letter == keyArray[10]:
                    decodedCharacters.append('k')
                elif letter == keyArray[11]:
                    decodedCharacters.append('l')
                elif letter == keyArray[12]:
                    decodedCharacters.append('m')
                elif letter == keyArray[13]:
                    decodedCharacters.append('n')
                elif letter == keyArray[14]:
                    decodedCharacters.append('o')
                elif letter == keyArray[15]:
                    decodedCharacters.append('p')
                elif letter == keyArray[16]:
                    decodedCharacters.append('q')
                elif letter == keyArray[17]:
                    decodedCharacters.append('r')
                elif letter == keyArray[18]:
                    decodedCharacters.append('s')
                elif letter == keyArray[19]:
                    decodedCharacters.append('t')
                elif letter == keyArray[20]:
                    decodedCharacters.append('u')
                elif letter == keyArray[21]:
                    decodedCharacters.append('v')
                elif letter == keyArray[22]:
                    decodedCharacters.append('w')
                elif letter == keyArray[23]:
                    decodedCharacters.append('x')
                elif letter == keyArray[24]:
                    decodedCharacters.append('y')
                elif letter == keyArray[25]:
                    decodedCharacters.append('z')
                elif letter == '#':
                    decodedCharacters.append(' ')
                else:
                    decodedCharacters.append(letter)
            
            decodedString = ''.join(decodedCharacters)
            print(f'''Decrypted Text: {decodedString}''')





