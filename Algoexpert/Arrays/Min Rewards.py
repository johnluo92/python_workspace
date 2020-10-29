'''Min Rewards

Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not ncessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules:

	1.) All students must receive at least one reward

	2.) any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or the right) with a lower score and must receive strictly fewwer rewards than an adjacaent student with a higher score.

Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules.

You can assume that all students have diference scores; in other words, the scores are all unique.
'''

# o(n) time | o(n) space
def minRewards(scores):
    rewards = [1]*len(scores)

    # move left to right
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i]>scores[j]:
            rewards[i] = rewards[j]+1

    # move right to left
    for i in reversed(range(len(scores)-1)):
        j = i+1
        if scores[i]>scores[j]:
            rewards[i] = max(rewards[i],rewards[j]+1)

    print(rewards)
    return sum(rewards)

array = [8, 4, 2, 1, 3, 6, 7, 9, 5]

print(minRewards(array)) # True