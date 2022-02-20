# Cipher Project

This project focuses on replicating a one-time pad (OTP), an encryption technique that requires the use of a single-use key (one-time pad) in order to  encrypt a message. The contains the following functions and descriptions.

## Broad Overview of Code

1. **generatePad** - This function takes in the arguments *file_name* and *pad_length* and creates a randomly generated key with uppercase letters used to encrypt/decrypt a message. The length of the key is determined by the *pad_length* and this key is saved to a file determined by the *file_name*. Note that the length of the key must be the same or greater than the length of the message. 

2.  **encipherShift** - This function takes in the arguments *message* and *pad* (as separate files) and converts both into their corresponding ascii number. Each letter in the message is shifted a certain number of spaces *to the right* depending on the number contained in the same index of the pad. Note that non-letters in the message are not changed and are contained in the final ouput. The final output is the encrypted message as a string.

3. **decipherShift** - Similarly to the encipherShift, this function takes in the arguments *message* and *pad_length*. The process is similar to the encipherShift function, instead, this time, the letters in the message are *shifted to the left* in order to decode the message. The final output is the decrypted message as a string.

## How to run tests
The main code was tested using pytest, and the tests are located in **test_cipher2.py**. In order to run this program, type in console: 

```pytest test_2.py```

Make sure that the current working directory is the same as the same as the one cipher.py is in.
