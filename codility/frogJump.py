# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    distance = Y-X
    if distance == 0:
        return 0
    if distance <= D:
        return 1

    if distance % D == 0:
        return distance // D
    
    return (distance // D) + 1
        

print(solution(10, 85, 30))