# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    numbank = {}

    for num in A:
        if num not in numbank:
            numbank[num] = True

    counter = 1

    for i in range(len(A)):
        if counter not in numbank:
            return counter
        counter += 1