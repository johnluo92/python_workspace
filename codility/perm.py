# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    mySet = set()
    for i in range(1, len(A)+1):
        mySet.add(i)

    for i in range(len(A)):
        digit = A[i]
        if digit in mySet:
            mySet.remove(digit)
        else:
            return 0

    if len(mySet) == 0:
        return 1
    return 0