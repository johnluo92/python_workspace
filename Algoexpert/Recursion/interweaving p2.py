def interweavingStrings(one, two, three):
    # Write your code here.
    
    cond = dfs_traverse(one, two, three, 0, 0)
    print(cond)
    return cond

def dfs_traverse(one, two, three, i,j):
    a,b = False, False
    
    print(i, j, len(three))
    
    k = i+j
    
    if k > len(three):
        return True
    
    if i < len(one):
        if three[k] == one[i]:
            a = dfs_traverse(one, two, three, i+1, j)
    if j < len(two):
        if three[k] == two[j]:
            b = dfs_traverse(one, two, three, i, j+1)

    return a or b


# one = "algoexpert"
# two = "your-dream-job"
# three = "your-algodream-expertjob"

# one = "a"
# two = "b"
# three = 'ac'

one = 'algoexpert'
two = 'your-dream-job'
three = 'your-algodream-expertjo'

# one = "aacaaaa"
# three = "aaaabacaaaaaaa" 
# two = "aaabaaa"

interweavingStrings(one, two, three)