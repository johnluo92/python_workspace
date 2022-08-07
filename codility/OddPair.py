# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num_bank = {}
    for item in A:
        if item not in num_bank:
            num_bank[item] = 1
        else:
            num_bank[item] += 1

    for key, value in num_bank.items():
        if value % 2 != 0:
            return value