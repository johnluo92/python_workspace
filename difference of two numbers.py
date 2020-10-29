def find_pair_diff(array, target):
    
    hashTable = {k for k in array}
    print(hashTable)
    
    for value in array:
        if value-target in hashTable:
            ans = (value, value-target)
            return ans
        
    return []

arr = [5, 20, 3, 2, 50, 80]
t = 78

print(find_pair_diff(arr, t))