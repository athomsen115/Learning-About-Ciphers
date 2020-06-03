#Hide a null cipher in a list of names


def loadNames(file):
    try:
        with open(file) as f:
            text = f.read().strip().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

def main():
    message = "Have your cake and eat it too"
    message = "".join(message.split())
    
    names = loadNames('supporters.txt')
    nameList = []
    nameList.append(names[0])
    
    count = 1
    #letter of message goes in the 2nd letter of the name, then the third, then is repeated
    for letter in message:
        for name in names:
            if len(name) > 2 and name not in nameList:
                if count % 2 == 0 and name[2].lower() == letter.lower():
                    nameList.append(name)
                    count += 1
                    break
                elif count % 2 != 0 and name[1].lower() == letter.lower():
                    nameList.append(name)
                    count += 1
                    break
    
    nameList.insert(3, 'stuart')
    nameList.insert(6, 'jacob')
    nameList.insert(9, 'robert')
    
    print("""
    Your Majesty,
    It is with great honor that I present the list of noble families who
    have undertaken the priviledge of supporting your cause and petition
    the usurper for your release from these tragic circumstances.
    """)
    
    print(*nameList, sep='\n')
    
if __name__ == "__main__":
    main()