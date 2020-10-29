
'''Knapsack Problem.py
'''

def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    knapsackValues = [[0 for i in range(capacity+1)] for i in range(len(items)+1)]
    
    for currentItem in range(1, len(knapsackValues)):
        
        currentWeight = items[currentItem-1][1]
        
        currentValue = items[currentItem-1][0]
        
        for currentCap in range(1, capacity+1):
            
            bestValueWeight = knapsackValues[currentItem-1][currentCap]
            
            if currentWeight > currentCap:
                
                knapsackValues[currentItem][currentCap] = bestValueWeight
            
            else:
                
                valueWithoutCurr = knapsackValues[currentItem-1][currentCap-currentWeight]
                
                testWeightValue = currentValue + valueWithoutCurr
                
                knapsackValues[currentItem][currentCap] = max(bestValueWeight, testWeightValue)
                
    for value in knapsackValues:
        print(value)
        
    return knapsackValues[-1][-1]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            return list(reversed(sequence))

item = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

print(knapsackProblem(item, capacity))