# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    minDiff = float('inf')
    total = sum(A)
    prefix, suffix = A[0], total-A[0]

    for i in range(1, len(A)):
        currDiff = abs(prefix - suffix)
        minDiff = min(minDiff, currDiff)
        prefix, suffix = prefix + A[i], suffix-A[i]
    return minDiff
    pass
