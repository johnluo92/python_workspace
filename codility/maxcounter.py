# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    max_counter = 0
    counters = [0 for i in range(N)]
    for i in range(len(A)):
        value = A[i]
        counter_inx = value-1
        if 1<= value <= N:
            counters[counter_inx] += 1
            current_counter = counters[counter_inx]
            max_counter = max(max_counter, current_counter)
        elif value == N + 1:
            counters = [max_counter for i in counters]

    return counters