'''Number of Ways to Make Change

Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.
'''

# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    array = [0 for i in range(n+1)]
    array[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                array[amount] += array[amount-denom]

    print(list(enumerate(array)))
    return array[n]

denoms = [1,2,5]

print(numberOfWaysToMakeChange(6, denoms)) # True