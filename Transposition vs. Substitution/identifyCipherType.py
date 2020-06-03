import sys
from collections import Counter

CUTOFF = 0.5 #arbitrary cutoff fraction of 6 most common letters in English

def load(filename):
    try:
        with open(filename) as f:
            return f.read().strip()
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
        
ciphertext = load('cipher11.txt')
sixMostCommon = Counter(ciphertext.lower()).most_common(6)
print("The 6 most commonly used letters in English are: ETAOIN")
print("Six most frequent letters in the ciphertext: {}", *sixMostCommon, sep='\n')

cipherMostCommon = {i[0] for i in sixMostCommon}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
    if letter in cipherMostCommon:
        count += 1
        
if (count / len(TARGET)) > CUTOFF:
    print("This is most likely the result of a TRANSPOSITION cipher")
else:
    print("This is most likely the result of a SUBSTITUTION cipher")