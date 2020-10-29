'''nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and nth number if the sum of the (n-1)th and (n-2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.
'''

# This is an input class. Do not edit.

def getNthFib(n):
    # Write your code here.
    nthFib = 0
    fibBuilder = [0,1]
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(2, n+1):
        nthFib = sum(fibBuilder)
        fibBuilder[0] = fibBuilder[1]
        fibBuilder[1] = nthFib
    print(fibBuilder[0])
    return fibBuilder[0]
    
    # 0 1 1 2 3 5 8
#     0 1 2 3 4 5 6

getNthFib(6)