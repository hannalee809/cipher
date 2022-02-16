import random
import string

# generatePad function 
def generatePad(pad_length):
    letters = string.ascii_uppercase
    print(''.join(random.choice(letters) for i in range(int(pad_length))))

    # put into a file


# Shift a letter by the designated amount, regardless of case
def shiftLetter(char,shift):

    # Get the ASCII number for the character
    ascii = ord(char)
    
    # If the ASCII code is an uppercase letter,
    # Shift and unshift by 65 so A=0 and Z=25
    if (ascii >= 65) and (ascii <= 90):
        shifted = (ascii - 65 + shift) % 26 + 65

    # If the ASCII code is a lowercase letter,
    # Shift an unshift by 97 so a=0 and z=25
    elif (ascii >= 97) and (ascii <= 122):
        shifted = (ascii - 97 + shift) % 26 + 97
    
    # If the ASCII code isn't a letter,
    # Don't shift it at all
    else:
        shifted = ascii

    # Return the shifted ASCII code as a character
    return chr(shifted)

# Shift all characters in a message by the designated amount, regardless of case
def shiftMessage(message,pad):
    # return "".join([shiftLetter(c,shift) for c in message])
    for message_letter, pad_number in zip(message, pad):
        print("".join[shiftLetter] )
        

def encipher(messagef,padf):
    f = open(padf)
    pad = f.read()
    m = open(messagef)
    message = m.read()
    finalMessage = []
    used = 0
    for i in message:
        i_index = message.index(i)
        i_num = ord(i)
        if ((i_num>=65) and (i_num<=90)) or ((i_num>=97) and (i_num<=122)):
            finalMessage.append(shiftLetter(i, ord(pad[used]) - 65))
            used += 1
        else:
            finalMessage.append(i)
            used += 1
    print("".join(finalMessage))
        

def decipher(messagef, padf):
    f = open(padf)
    pad = f.read()
    m = open(messagef)
    message = m.read()
    finalMessage = []
    used = 0
    for i in message:
        i_index = message.index(i)
        i_num = ord(i)
        if ((i_num>=65) and (i_num<=90)) or ((i_num>=97) and (i_num<=122)):
            finalMessage.append(shiftLetter(i, -(ord(pad[used]) - 65)))
            used += 1
        else:
            finalMessage.append(i)
            used += 1
    print("".join(finalMessage))

decipher(messagef = "HELLO WORLD", padf = "AAAAAAAAAAA")
#decipher(messagef = input("Message: "), padf = input("Pad: "))

        
