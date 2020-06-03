import math
from itertools import permutations, product

numCols = 4
columns = [x for x in range(1, numCols + 1)]
print("Columns: {}".format(columns))

def perms(columns):
    results = []
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results

def main():
    columnCombos = perms(columns)
    print(*columnCombos, sep='\n')
    print("Factorial of number of columns without negatives: {}".format(math.factorial(numCols)))
    print("Number of column combinations = {}".format(len(columnCombos)))
    print("To understand the difficulty behind brute force, we can see just how many options are available for the key")

if __name__ == '__main__':
    main()