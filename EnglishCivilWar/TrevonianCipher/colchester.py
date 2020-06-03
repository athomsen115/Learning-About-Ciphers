import sys

def loadText(file):
    try:
        with open(file) as f:
            text = f.read().strip()
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        
def main():
    filename = input("Enter filename for message to translate: ")
    inputMessage = loadText(filename)
    
    print("Original Message: {}".format(inputMessage))
    
    message = inputMessage.split()
    end = len(message)
    
    increment = int(input("Input max word and letter possition to check: (eg. every 1 or 1, or every 2 of 2)"))
    
    for i in range(1, increment + 1):
        print("Using increment letter {} of word {}".format(i, i))
        count = i - 1
        location = i - 1
        for index, word in enumerate(message):
            if index == count:
                if location < len(word):
                    print("Letter: {}".format(word[location]))
                    count += i
                else:
                    print("Interval doesn't work")

if __name__ == "__main__":
    main()