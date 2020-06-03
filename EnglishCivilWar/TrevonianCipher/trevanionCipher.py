import sys, string
#Trevonian ciphers form a message using every third level after a punctuation mark
#Rules: initiate a leter count with every punctuation mark, reset the count if a punctuation mark is encountered, punctuation marks cannot be part of the plaintext message

def loadText(file):
    try:
        with open(file) as f:
            return f.read().strip()
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        
def main():
    file = input("Name of file to translate: ")
    text = loadText(file)
    
    
    print ("Original Message: {}".format(text))
    message = ''.join(text.split())
    while True:
        letterCount = input("How many letters after the punctuation should we look? (default is 3)")
        if letterCount == '':
            letterCount = '3'
        if letterCount.isdigit():
            letters = int(letterCount)
            break
        else:
            ("Please input a number...")
    
    solveTrevonianCipher(message, letters)
            
def solveTrevonianCipher(message, letterCount):
    for x in range(1, letterCount + 1):
        translation = ''
        count = 0
        punct = False
        for char in message:
            if char in string.punctuation:
                count = 0
                punct = True
            elif punct is True:
                count += 1
            if count == x:
                translation += char
                
        print("Offset is: {}, Plaintext: {}".format(x, translation))
    print()

if __name__ == '__main__':
    main()  
        
        