import sys

ciphertext = "REST TRANSPORT YOU GOODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"
COL = 4
ROW = 5
key = '-1 2 -3 4' # negative number means reverse the row

def main():
    print("Ciphertext: {}".format(ciphertext))
    #print("Trying {} columns".format(COL))
    #print("Trying {} rows".format(ROW))
    #print("Trying Key: {}".format(key))
    
    cipherlist = list(ciphertext.split())
    validateRowCol(cipherlist)
    keyInt = keyToInt(key)
    translationMatrix = buildMatrix(keyInt, cipherlist)
    plaintext = decrypt(translationMatrix)

    #print("Key Length = {}".format(len(keyInt)))
    print("Plaintext: {}".format(plaintext))
    plaintext_decoded = translateCode(plaintext)
    print("Plaintext Code Words Translated: {}".format(plaintext_decoded))
    
def validateRowCol(cipherlist):
    factors = []
    lenCipher = len(cipherlist)
    for i in range(2, lenCipher):
        if lenCipher % i == 0:
            factors.append(i)
    #print("Length of Cipher: {}".format(lenCipher))
    #print("Acceptable column/row values include: {}".format(factors))
    print()
    
    if ROW*COL != lenCipher:
        print("[ERROR] Input columns and rows not factors of length of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def keyToInt(key):
    keyInt = [int(i) for i in key.split()]
    keyIntLow = min(keyInt)
    keyIntHigh = max(keyInt)
    
    if (len(keyInt) != COL) or (keyIntLow < -COL) or (keyIntHigh > COL) or (0 in keyInt):
        print("[ERROR] Problem with key. Terminating program.", file=sys.stderr)
        sys.exit(2)
    else:
        return keyInt
    
def buildMatrix(keyInt, cipherlist):
    translation = [None] * COL
    start = 0
    stop = ROW
    
    for k in keyInt:
        if k < 0:
            colItems = cipherlist[start:stop]
        elif k > 0:
            colItems = list((reversed(cipherlist[start:stop])))
        translation[abs(k) - 1] = colItems
        start += ROW
        stop += ROW
    return translation

def decrypt(translationMatrix):
    plaintext = ''
    for i in range(ROW):
        for colItems in translationMatrix:
            word = str(colItems.pop())
            plaintext += word + ' '
    
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
