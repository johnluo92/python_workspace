import sys
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    knapsack = [[0 for i in range(capacity+1)] for j in range(len(items))]
    
    for i in range(len(items)):
        item = items[i]
        for j in range(1, capacity+1):
            current_cap = j
            item_weight = item[1]
            if i != 0:
                knapsack[i][j] = knapsack[i-1][j]
            if current_cap >= item_weight:
                test_value = item[0]
                if i == 0:
                    knapsack[i][j] = test_value
                    continue
                prev_wight = current_cap - item_weight
                test_value += knapsack[i-1][prev_wight]
                knapsack[i][j] = max(knapsack[i][j], test_value)
    
    for row in knapsack:
        print(row)
        
    maxval = knapsack[-1][-1]
    item_indices = constructIndices(items, capacity, knapsack)
    
    return [maxval, item_indices]

def constructIndices(items, capacity, knapsack):
    item_idxs = []
    value = knapsack[-1][-1]
    item_idx = len(items)-1
    curr_cap = capacity
    
    while value >= 1:
        if item_idx - 1 >= 0:
            if knapsack[item_idx][curr_cap] == knapsack[item_idx-1][curr_cap]:
                item_idx -= 1
                continue
        item_idxs.append(item_idx)
        curr_cap -= items[item_idx][1]
        value -= items[item_idx][0]
        item_idx -= 1
            
            
    item_idxs.reverse()
    print(item_idxs)
    return item_idxs


items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity=  10

print(knapsackProblem(items, capacity))
