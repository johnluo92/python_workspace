import sympy

def permutationPrimes(string):

    permutations = []
    print(isPrime(string))

    for i in range(1, len(string)+1):
        left = int(string[0:i])
        prime = sympy.isprime(left)
        if prime:
            generatePerms(string, i, permutations, [left])

    for perm in permutations:
        print(perm)
    return permutations

def generatePerms(string, idx_i, permutations, current):
    if idx_i == len(string):
        permutations.append(current)
        return

    for j in range(idx_i+1, len(string)+1):
        right = int(string[idx_i:j])
        prime = sympy.isprime(right)
        if isPrime(right):
            current.append(right)
            generatePerms(string, j, permutations, current)
            current.pop()


def isPrime(string):
    num = int(string)
    return (num % 2 != 0 and num != 1) or num == 2

num = '21373'
num = '323'
# num = '2'

permutationPrimes(num)

# print(isPrime(num))