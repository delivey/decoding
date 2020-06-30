import sys

if len(sys.argv) > 2:
    print("Amount of arguments supplied is greater than 2")
    sys.exit(0)

def base64decoder(encodedString):

    def dec_to_bin(x): # Function for converting decimal to binary
        return "{0:08b}".format(x)

    def bin_to_dec(x): # Function for converting binary to decimal
        decimal = 0
        binary = list(str(x))
        binary = binary[::-1]
        power = 0
        for number in binary:
            if number == '1':
                decimal += 2**power    
            power += 1
        return decimal

    b64dict = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
        "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
        "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
        "Y": 24, "Z": 25,

        "0": 52, "1": 53, "2": 54, "3": 55, "4": 56, "5": 57, "6": 58, "7": 59,
        "8": 60, "9": 61, "+": 62, "/": 63
    }

    ascDict = {i: chr(i) for i in range(129)}

    conct = ""
    for char in encodedString: # For each character in the inputted text
        if char.islower(): # Checks if the character is lowercase
            asc = b64dict[char.upper()] + 26 # If it is, converts it to uppercase and adds 26 to the decimal value
        else: # If the character isn't lowercase
            asc = b64dict[char] # Looks it up in the 'b64dict' dictionary
        binr = dec_to_bin(asc) # Converts the value to binary
        wtpre = str(binr[2:]) # Removes the first two characters of the binary string
        conct += wtpre # Adds the 'without prefix' string to the whole string grouped.

    divd = [] # The list for the divided strings
    for i in range(0, len(conct), 8):
        divd.append(conct[i:i + 8])

    # if len(divd[-1]) < 8:
        # divd.remove(divd[-1])
    strList = []
    for i in divd: # For each element in the divided string list
        strList.append(ascDict[bin_to_dec(i)])
    return ''.join(strList)

print(base64decoder(sys.argv[1]))
