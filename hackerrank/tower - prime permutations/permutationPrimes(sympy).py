from sympy import isprime

def permutationPrimes(string):

    permutations = []

    for i in range(1, len(string)+1):
        left = string[0:i]
        if isprime(int(left)):
            generatePerms(string, i, permutations, [left])

    print('print sets')
    for permset in permutations:
        print(permset)
    return permutations

def generatePerms(string, i, permutations, current):
    if i == len(string):
        permutations.append(current[:])
        return

    for j in range(i+1, len(string)+1):
        right = string[i:j]
        if isprime(int(right)):
            current.append(right)
            generatePerms(string, j, permutations, current)
            current.pop()


def isPrime(string):
    num = int(string)
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

string = '11373123231211'
# string = '21373'
# string = '323'
# string = '53'
# string = '5'
# string = '2'

print(f'{string} is a prime:', isPrime(string))
print(f'verifying:', isprime(int(string)))
print()
permutationPrimes(string)

# print(isPrime(num))