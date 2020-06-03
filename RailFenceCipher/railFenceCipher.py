
plaintext = "Let us cross over the river and rest under the shade of the trees"

def main():
    message = prepPlaintext(plaintext)
    rails = buildRails(message)
    encrypt(rails)

def prepPlaintext(plaintext):
    message = ''.join(plaintext.split())
    message = message.upper()
    print("Plaintext: {}".format(plaintext))
    return message

def buildRails(message):
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails

def encrypt(rails):
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print("Ciphertext: {}".format(ciphertext))

if __name__ == '__main__':
    main()