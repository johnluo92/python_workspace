def maxSumIncreasingSubsequence(array):
    # Write your code here.
    max_sum_arr = array[:]
    sequences = [None for _ in array]

    max_idx = 0
    max_sum = 0
    
    for i in range(1, len(array)):
        current_num = array[i]
        for j in range(0, i):
            other_num = array[j]
            if current_num > other_num and current_num + max_sum_arr[j] >= max_sum_arr[i]:
                max_sum_arr[i] = max_sum_arr[j] + current_num
                sequences[i] = j
        print(sequences)
        if max_sum_arr[i] > max_sum_arr[max_idx]:
            print('hi', i)
            max_idx = i
    sequence = build_sequence(array, sequences, max_idx)
    print(max_sum_arr[max_idx], sequence)
    return [max_sum, sequence]

def build_sequence(array, sequences, current_idx):
    sequence = []
    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]
        print(current_idx)
    ans = list(reversed(sequence))
    return ans


arr = [10, 70, 20, 30, 50, 11, 30]
# arr = [-1, 1]
maxSumIncreasingSubsequence(arr)