"""Max Sum Increasing Subsequence

Write a function that takes in a non-empty array of integers and returns the greatest sum that can be generated from
a strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
order as they appear in the array. For instance, the numbers [1,2,4] form a subsequence of the array [1,2,3,4],
and so do the numbers [2,4]. Note that a single number in an array and the array itself are both valid subsequences
of the array. """


def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sequences = [None for x in array]
    sums = array[:]
    currentMaxID = 0

    for i in range(len(array)):
        current_num = array[i]
        for j in range(0, i):
            prev_num = array[j]
            if current_num > prev_num and prev_num + current_num >= sums[i]:
                sums[i] = current_num + sums[j]
                # the last number that was part of the sequence
                sequences[i] = j

        if sums[i] > sums[currentMaxID]:
            current_max_id = i

    return [max(sums), getIncreasingSequence(array, sequences, current_max_id)]


def getIncreasingSequence(array, sequences, currentMaxID):
    sequence = []
    while currentMaxID is not None:
        sequence.append(array[currentMaxID])
        currentMaxID = sequences[currentMaxID]
    return list(reversed(sequence))


array = [10, 70, 20, 30, 50, 11, 30]

print(maxSumIncreasingSubsequence(array))  # True
