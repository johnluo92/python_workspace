'''Min Number of Coins for Change

Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the smallest number of oins needed to make change for (to sum up to) that target amount using the given coin denominations.

Note that you have access ti an unlimited amount of coins. If the denominations are [1,2,5], you have unlimited amount of 1s, 5s, and 10s.
'''

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	myDenoms = [float('inf') for i in range(n+1)]
	myDenoms[0] = 0
	for denom in sorted(denoms):
		for amount in range(len(myDenoms)):
			if amount >= denom:
				myDenoms[amount] = min(myDenoms[amount], myDenoms[amount-denom]+1)
	print(myDenoms)
	print(myDenoms[n])
	return myDenoms[n] if myDenoms[n] != float('inf') else -1

denoms = [1,5,10]

print(minNumberOfCoinsForChange(7, denoms)) # True