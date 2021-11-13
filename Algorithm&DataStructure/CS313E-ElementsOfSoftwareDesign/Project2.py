# File: Project2.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 04/10/2021
# Date Last Modified: 04/12/2021
# Description of Program:

import random

# A global constant defining the alphabet.
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"
# You are welcome to use the following two auxiliary functions, or
# define your own.   You don't need to understand this code at this
# point in the semester.
def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt.

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey()):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__key = key
    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)
    def getKey( self ):
        return self.__key

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey):
            self.__key = newKey

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        str = ''
        for word in plaintext:
            if 97 <= ord(word) <= 122:
                str += self.__key[ord(word) - 97]
            elif 65 <= ord(word) <= 90:
                str += chr(ord(self.__key[ord(word) - 65]) - 32)
            else:
                str += word
        return str

    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        str = ''
        for i in ciphertext:
            for j in self.__key:
                if 97 <= ord(i) <= 122:
                    if i == j:
                        str += chr(self.__key.index(j) + 97)
                elif 65 <= ord(i) <= 90:
                    if i == chr(ord(j) - 32):
                        str += chr(self.__key.index(j) + 65)
                else:
                    str += i
                    break
        return str

def main():
     """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit."""
     a = SubstitutionCipher()
     # text = input('text = ' )
     while True:
         command = input('Enter a command (getKey, changeKey, encrypt, decrypt, quit): ')
         command1 = ''
         for i in range(len(command)):
             if 65 <= ord(command[i]) <= 90:
                 command1 += (chr(ord(command[i]) + 32))
             else:
                 command1 += command[i]
         if command1 == 'getkey' :
             print('  Current cipher key: ', a.getKey())
         elif command1 == 'changekey':
             while True:
                 b = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                 if b == 'quit':
                     break
                 if b == 'random':
                     r = makeRandomKey()
                     print('    New cipher key: ', r)
                     a.setKey(r)
                     continue
                 if  isLegalKey(b) is False:
                     print('    Illegal key entered. Try again!')
         elif command1 == 'encrypt':
             text = input('  Enter a text to encrypt: ')
             print('    The encrypted text is: ', a.encryptText(text))
         elif command1 == 'decrypt':
             text = input('  Enter a text to decrypt: ')
             print('    The decrypted text is: ', a.decryptText(text))
         elif command1 == 'quit':
             break
         else:
             print('  Command not recognized. Try again!')
     print('Thanks for visiting!')



main()