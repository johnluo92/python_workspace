# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6

    if len(A) == 0:
        return []
    array_size = len(A)
    if K % array_size == 0:
        return A

    K = K % array_size
    new_arr = [None for i in A]


    for i in range(len(A)):
        if i+K >= array_size:
            new_arr[i+K - array_size] = A[i]
        else:
            new_arr[i+K] = A[i]
        
    return new_arr



A = [3, 8, 9, 7, 6]
K = 300

print(solution(A, K))