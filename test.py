
def minRewards(scores):

    rewards = [1]*len(scores)

    for i in range(1, len(scores)):
        j = i - 1
        if scores[i]>scores[j]:
            rewards[i] = rewards[j]+1

    print(rewards)
            
    for i in reversed(range(len(scores)-1)):
        j = i+1
        if scores[i]>scores[j]:
            rewards[i] = max(rewards[i],rewards[j]+1)
        print(i, j)
        print(rewards)
    return sum(rewards)

arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(list(enumerate(arr)))
minRewards(arr)