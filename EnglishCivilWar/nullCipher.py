import random, string

def load_dictionary(file):
    try:
        with open(file) as f:
            text = f.read().strip().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        
def main():
    message = "panel at east end of chapel slides"
    
    codedMessage = ''
    for char in message:
        if char in string.ascii_letters:
            codedMessage += char
    
    print(codedMessage)
    codedMessage = ''.join(codedMessage.split())
    
    words = load_dictionary('dictionary.txt')
    vocab = []
    for letter in codedMessage:
        length = random.randint(6, 10)
        for word in words:
            if len(word) == length and word[2].lower() == letter.lower() and word not in vocab:
                vocab.append(word)
                break
            
    if len(vocab) < len(codedMessage):
        print("Word list is too small. Try larger dictionary or shorter message")
    else:
        print("Hint: check every 3rd letter for the coded message")
        print("Vocaulary words: ", *vocab, sep='\n')
        
if __name__ == '__main__':
    main()
    