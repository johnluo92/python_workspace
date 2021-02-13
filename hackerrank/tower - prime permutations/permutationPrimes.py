from sympy import isprime
import time


def permutationPrimes(string):
    permutations = []
    primeSet = set()

    for i in range(1, len(string) + 1):
        left = int(string[0:i])
        if isPrime(left, primeSet):
            generatePerms(string, i, permutations, [left], primeSet)

    print('print sets')
    for permset in permutations:
        print(permset)
    return permutations


def generatePerms(string, i, permutations, current, primeSet):
    if i == len(string):
        permutations.append(current[:])
        return

    for j in range(i + 1, len(string) + 1):
        right = int(string[i:j])
        if isPrime(right, primeSet):
            current.append(right)
            generatePerms(string, j, permutations, current, primeSet)
            current.pop()


def isPrime(num, primeSet):
    if num in primeSet:
        return True
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, (num // 2)):
        if num % i == 0:
            return False
    primeSet.add(num)
    return True


string = '135029'
# string = '21373'
# string = '323'
# string = '53'
# string = '5'
# string = '2'
start = time.time()
# print(f'{string} is a prime:', isPrime(string, set()))
# print(f'verifying:', isprime(int(string)))
print()
permutationPrimes(string)
end = time.time()

total = start - end
print(total)
# print(isPrime(num))
