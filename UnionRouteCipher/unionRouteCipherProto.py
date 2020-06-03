#Understanding how the route cipher works, using numbers to represent the words
#Each number is put into a matrix (which affects how the ciphertext is translated), and then the matrix is read in the described order to produce the plaintext
#The translation matrix is built as the string is unraveled (across X rows, and then wrapping into the next column (which requires reversing of the order of elements in every other list))
#The key is used to tell the algorithm which lists to reverse when building the translation matrix
ciphertext = "20 15 10 5 0 1 6 11 16 21 22 17 12 7 2 3 8 13 18 23 24 19 14 9 4"

cipherlist = list(ciphertext.split())

COL = 5
ROW = 5

key = '-1 2 -3 4 -5' # negative number means reverse the row
translation = [None] * COL
plaintext = ''
start = 0
stop = ROW

keyInt = [int(i) for i in key.split()]

for k in keyInt:
    if k < 0:
        colItems = cipherlist[start:stop]
    elif k > 0:
        colItems = list((reversed(cipherlist[start:stop])))
    translation[abs(k) - 1] = colItems
    start += ROW
    stop += ROW
    
print("Ciphertext: {}".format(ciphertext))
print("Translation Matrix: ", *translation, sep='\n')
print("Key Length = {}".format(len(keyInt)))

for i in range(ROW):
    for colItems in translation:
        word = str(colItems.pop())
        plaintext += word + ' '

print("Plaintext: {}".format(plaintext))