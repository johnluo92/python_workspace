# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    traversable = set()
    for i in range(1, X+1):
        traversable.add(i)

    for i in range(len(A)):
        location = A[i]
        if location in traversable:
            traversable.remove(location)
        if len(traversable) == 0:
            return i
    return -1