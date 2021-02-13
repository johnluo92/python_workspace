from sympy import isprime
import time

def permutationPrimes(string):

    permutations = []
    primeSet = set()

    for i in range(1, len(string)+1):
        left = int(string[0:i])
        if isprime(left):
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
        right = int(string[i:j])
        if isprime(right):
            current.append(right)
            generatePerms(string, j, permutations, current)
            current.pop()


def isPrime(string, primeSet):
    if string in primeSet:
        return True
    num = int(string)
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, (num//2)):
        if num % i == 0:
            return False
    primeSet.add(string)
    return True

string = '11333111'
string = '331777115511'
string = '135029'
# string = '1350297079989171477791892123929141605573631151125933376097791877830238462471373933362476484818693477173990672289892448124097556197582379957168911392680312103962394732707409889862447273901522659'
# string = '323'
# string = '53'
# string = '5'
# string = '2'
start = time.time()
print(f'{string} is a prime:', isPrime(string, set()))
print(f'verifying:', isprime(int(string)))
print()
permutationPrimes(string)
end = time.time()

total = start-end
print(total)
# print(isPrime(num))