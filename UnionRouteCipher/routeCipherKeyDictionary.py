columnOrder = "1 3 4 2"

key = dict()

columns = [int(i) for i in columnOrder.split()]
for col in columns:
    while True:
        key[col] = input("Direction to read Column {} (u = up, d = down): ".format(col).lower())
        if key[col] == 'u' or key[col] == 'd':
            break
        else:
            print("Input shoud be 'u' or 'd'")
            
    print("{} {}".format(col, key[col]))