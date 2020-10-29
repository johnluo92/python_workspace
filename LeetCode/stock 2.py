# # stock 2.py

# class Solution:
#     def maxProfit(self, prices):
#     	print(prices)
#     	best_with = -float('inf')
#     	best_without = 0

#     	for x in prices:
#     		best_with = max(best_with, best_without - x)
#     		best_without = max(best_without, best_with + x)

#     		print(f'when x = {x} \nbest with stock:   {best_with} \nbest without stock: {best_without}\n')

#     	print()
#     	print(best_without)

class Solution:
    def maxProfit(self, prices, k = None):

        if k is None:
            maxTran = (len(prices)//2) + 1
        else:
            maxTran = k+1

        profits = [[0 for p in prices] for k in range(maxTran)]

        for i in profits:
            print(i)

        print()
        
        for tran in range(1, maxTran):
            max_diff = -float('inf')
            for day in range(1, len(prices)):
                max_diff = max(max_diff, profits[tran-1][day-1] - prices[day-1])
                profits[tran][day] = max(profits[tran][day-1], max_diff + prices[day])

        for i in profits:
            print(i)
        print()


Solution().maxProfit([7,1,5,3,6,4])
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]

# [0, 0, 0, 0, 0, 0]
# [0, 0, 4, 4, 5, 5]
# [0, 0, 4, 4, 7, 7]
# [0, 0, 4, 4, 7, 7]

Solution().maxProfit([5, 11, 3, 50, 60, 90], 2)
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]

# [0, 0, 0, 0, 0, 0]
# [0, 6, 6, 47, 57, 87]
# [0, 6, 6, 53, 63, 93]

