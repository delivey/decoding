import string
import sys

#TODO: fix capital letter issues

def rot13(x):
    alphabet = list(string.ascii_letters)

    nUi = ""
    for letter in x:
        ind = alphabet.index(letter)
        added = ind + 13
        if added > len(alphabet):
            added = added - len(alphabet)
        nUi += str(alphabet[added])
    return nUi

print(rot13(sys.argv[1]))