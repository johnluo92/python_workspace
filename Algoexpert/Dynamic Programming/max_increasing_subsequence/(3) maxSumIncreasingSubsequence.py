'''
given  [10, 70, 20, 30, 50, 11, 30]

return the greatest sum that can be generated
as well as an array of the numbers in that subsequence

so the answer for the first part would be 110
because the longest subsequence is 10, 20, 30, 50

ouput: [110, [10, 20, 30, 50]]
'''

def maxSumIncreasingSubsequence(array):
    # Write your code here.
    max_sums = array[:]

    # [10, 70, 20, 30, 50, 11, 30]
    # [10, 80, 30, 60, 110, 21, 60]
    # [None,0, 0,  2,  3,   0,  2]

    sequence = [None for _ in array]
    [None, 0]
    max_sum_idx = 0

    for i in range(len(array)):
        current = array[i]
        for j in range(0, i):
            other = array[j]
            if current > other and current + max_sums[j] > max_sums[i]:
                max_sums[i] = current + max_sums[j]
                sequence[i] = j
        if max_sums[max_sum_idx] < max_sums[i]:
            max_sum_idx = i

    max_num = max_sums[max_sum_idx]
    subsequence = buildSequence(array, sequence, max_sum_idx)

    print([max_num, subsequence])
    return [max_num, subsequence]

def buildSequence(array, sequence, current_idx):
    answer = []
    while current_idx is not None:
        num = array[current_idx]
        answer.append(num)
        current_idx = sequence[current_idx]
    answer = list(reversed(answer))
    return answer

arr = [10, 70, 20, 30, 50, 11, 30]
maxSumIncreasingSubsequence(arr)

# --------------------------------------------------------------------------------------

# def maxIncreasingSubsequence(array):





# arr = [10, 70, 20, 30, 50, 11, 30]
# maxSumIncreasingSubsequence(array):