import math, itertools

#The rail fence follows a simple zig-zag pattern with the letters. 
#So if we can create the two rails, by splitting the message in half, we can then zig-zag to find the message

ciphertext = "LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"

def main():
    message = prepCipher(ciphertext)
    row1, row2 = splitRails(message)
    decrypt(row1, row2)

def prepCipher(ciphertext):
    message = ''.join(ciphertext.split())
    print("Ciphertext: {}".format(ciphertext))
    return message

def splitRails(message):
    row1Len = math.ceil(len(message)/2)
    row1 = (message[:row1Len])
    row2 = (message[row1Len:])
    return row1, row2

def decrypt(row1, row2):
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())
    if None in plaintext:
        plaintext.pop()
    print("Rail 1: {}".format(row1))
    print("Rail 2: {}".format(row2))
    print("Plaintext: {}".format(''.join(plaintext)))

if __name__ == '__main__':
    main()