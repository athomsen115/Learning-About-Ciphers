import sys


#Message is "GUARD ADAM THEM THEY AT WAYLAND BROWN FOR KISSING VENUS CORESPONDENTS AT NEPTUNE ARE OFF NELLY TURNING UP CAN GET WHY DETAINED TRIBUNE AND TIMES RICHARDSON THE ARE ASCERTAIN AND YOU FILLS BELLY THIS IF DETAINED PLEASE ODOR OF LUDLOW COMMISSIONER"
# GUARD is used to indicate the size of the rectangle (5 columns) and that every 8th word is null (ignored)

ciphertext = "ADAM THEM THEY AT WAYLAND BROWN FOR VENUS CORESPONDENTS AT NEPTUNE ARE OFF NELLY UP CAN GET WHY DETAINED TRIBUNE AND RICHARDSON THE ARE ASCERTAIN AND YOU FILLS THIS IF DETAINED PLEASE ODOR OF LUDLOW"
#message length = 24
COL = 5
ROW = 7
key = '-1 2 -5 4 -3' # negative number means reverse the row

def main():
    print("Ciphertext: {}".format(ciphertext))
    print("Trying {} columns".format(COL))
    print("Trying {} rows".format(ROW))
    print("Trying Key: {}".format(key))
    
    cipherlist = list(ciphertext.split())
    validateRowCol(cipherlist)
    keyInt = keyToInt(key)
    translationMatrix = buildMatrix(keyInt, cipherlist)
    plaintext = decrypt(translationMatrix)

    print("Key Length = {}".format(len(keyInt)))
    print("Plaintext: {}".format(plaintext))
    plaintextDecoded = translateCode(plaintext)
    print("Plaintext Code Words Translated: {}".format(plaintextDecoded))
    
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

def keyToInt(key):
    keyInt = [int(i) for i in key.split()]
    keyIntLow = min(keyInt)
    keyIntHigh = max(keyInt)
    
    if (len(keyInt) != COL):
        print("[ERROR] Problem with key (error 1). Terminating program.", file=sys.stderr)
        print(len(keyInt), file=sys.stderr)
        sys.exit(2)
    elif (keyIntLow < -COL):
        print("[ERROR] Problem with key (error 2). Terminating program.", file=sys.stderr)
        sys.exit(2)
    elif (keyIntHigh > COL):
        print("[ERROR] Problem with key (error 3). Terminating program.", file=sys.stderr)
        sys.exit(2)
    elif (0 in keyInt):
        print("[ERROR] Problem with key (error 4). Terminating program.", file=sys.stderr)
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
    for word in plaintext.split(' ')[:-4]:
        if word == 'WAYLAND':
            word = 'CAPTURED'
        elif word == 'NEPTUNE':
            word = 'RICHMOND'
        elif word == 'VENUS':
            word = 'COLONEL'
        elif word == 'ODOR':
            word = 'VICKSBURG'
        elif word == 'ADAM':
            word = 'PRESIDENT OF THE UNITED STATES'
        elif word == 'NELLY':
            word == '4:30 p.m.'
        text += word.lower() + ' '
    return text
       
if __name__ == '__main__':
    main()
