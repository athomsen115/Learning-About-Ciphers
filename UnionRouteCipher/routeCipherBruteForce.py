#Brute Force Version of figuring out the translation. Only one answer will be correct, and with codewords it is even harder to decrypt
import sys
from itertools import permutations, product

ciphertext = "REST TRANSPORT YOU GOODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"
COL = 4 # Number of columns believed to be in the transposition matrix
ROW = 5 # number of rows believed to be in the transposition matrix
key = '-1 2 -3 4' # negative number means reverse the row

def main():
    print("Ciphertext: {}".format(ciphertext))
    
    cipherlist = list(ciphertext.split())
    validateRowCol(cipherlist)
    plaintext = decrypt(cipherlist)
    
def validateRowCol(cipherlist):
    factors = []
    lenCipher = len(cipherlist)
    for i in range(2, lenCipher):
        if lenCipher % i == 0:
            factors.append(i)
    print("Length of Cipher: {}".format(lenCipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    
    if ROW*COL != lenCipher:
        print("[ERROR] Input columns and rows not factors of length of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def perms(COL):
    results = []
    columns = [x for x in range(1, COL + 1)]
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results      

def decrypt(cipherlist):
    columnCombos = perms(COL)
    for key in columnCombos:
        plaintext = ''
        translation = [None] * COL
        start = 0
        stop = ROW
        for k in key:
            if k < 0:
                colItems = cipherlist[start:stop]
            elif k > 0:
                colItems = list((reversed(cipherlist[start:stop])))
            translation[abs(k) - 1] = colItems
            start += ROW
            stop += ROW
        for i in range(ROW):
            for colItems in translation:
                word = str(colItems.pop())
                plaintext += word + ' '
        print("Using Key: {}".format(key))
        print("Translated Plaintext: {}".format(plaintext))
        plaintextDecoded = translateCode(plaintext)
        print("Plaintext Code Words Translated: {}".format(plaintextDecoded))
    print("Number of Results: {}".format(len(columnCombos)))
    return plaintext

def translateCode(plaintext):
    text = ''
    for word in plaintext.split(' '):
        if word == 'VILLAGE':
            word = 'ENEMY'
        elif word == 'ROANOKE':
            word = 'CAVALRY'
        elif word == 'GOODWIN':
            word = 'TENNESSEE'
        elif word == 'SNOW':
            word = "REBELS"
        text += word + ' '
    return text
       
if __name__ == '__main__':
    main()
