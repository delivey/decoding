# Code written by delivey
# https://github.com/delivey

import string
import sys

#TODO: still have to fix weird list index out of range error

def rot13(x):
    upAbet = list(string.ascii_uppercase)
    lowAbet = list(string.ascii_lowercase)

    nUi = ""
    for letter in x:
        if letter.islower():
            alphabet = lowAbet
        elif letter.isupper():
            alphabet = upAbet

        ind = alphabet.index(letter)
        added = ind + 13
        if added > len(alphabet):
            added = added - len(alphabet)
        nUi += str(alphabet[added])
    return nUi

print(rot13(sys.argv[1]))