def smallestMissingPositiveInteger(array):
    mynums = set()

    for num in array:
        if num in mynums:
            continue
        mynums.add(num)

    smallest = None
    for i in range(1, len(array)+1):
        if i in mynums:
            smallest = i
            continue
        else:
            return i

    return smallest+1

arr = [1, 3, 6, 4, 1, 2] # 5 because 5 is the smallest positive int not in arr
# arr = [1, 2, 3]
# arr = [-1, -3]
print(smallestMissingPositiveInteger(arr))