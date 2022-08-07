# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    temp = format(N, 'b')
    # print(temp)
    left_idx, right_idx = 0, 0
    max_counter = 0

    for i in range(len(temp)):
        if temp[i] == '1':
            right_idx = i
            current = right_idx - left_idx - 1
            max_counter = max(max_counter, current)
            left_idx = i
        if temp[i] == '0':
            continue

    return max_counter


print(solution(1041))