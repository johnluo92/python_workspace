#interweaving strings

def interweavingStrings(one, two, three):
    # Write your code here.
	if len(one)+len(two) != len(three):
		return False
	
	cache = [[None for i in range(len(two)+1)] for i in range(len(one)+1)]
	return isInterwoven(one, two, three, 0, 0, cache)

def isInterwoven(one, two, three, i, j, cache):
	print(cache)

	if cache[i][j] is not None:
		return cache[i][j]
	
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		cache[i][j] = isInterwoven(one, two, three, i+1, j, cache)
		if cache[i][j]:
			return True
		
	if j < len(two) and two[j] == three[k]:
		cache[i][j] = isInterwoven(one, two, three, i, j+1, cache)
		return cache[i][j]
	
	cache[i][j] = False
	return False


def sametwostrings(one, two, three):
    
    if len(one) + len(two) != len(three):
        return False
    
    return depthFirstHelper(one, two, three, 0, 0)

def depthFirstHelper(one, two, three, i, j):
    k = i + j
    print(one[i], two[j], three[k])
    
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
        if depthFirstHelper(one, two, three, i+1, j):
            return True
        
    if j < len(two) and two[j] == three[k]:
        return depthFirstHelper(one, two, three, i, j + 1)
    
    return False
# ------------------------------------------------------------
def interweavingStrings(one, two, three):
    # Write your code here.
    if len(one)+len(two) != len(three):
        return False
    
    cache = [[None for j in range(len(two)+1)] for i in range(len(one)+1)]
    return isInterwoven(one, two, three, 0, 0, cache)

def isInterwoven(one, two, three, i, j, cache):
    for line in cache:
        print(line)
    print()
    if cache[i][j] is not None:
        return cache[i][j]
    
    k = i + j
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
        cache[i][j] = isInterwoven(one, two, three, i+1, j, cache)
        if cache[i][j]:
            return True
        
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = isInterwoven(one, two, three, i, j+1, cache)
        return cache[i][j]
    
    cache[i][j] = False
    return False


one = "algoexpert"
one = 'aaa'
two = "your-dream-job"
two = 'aaaf'
three = "your-algodream-expertjob"
three = 'aaafaaa'

print(interweavingStrings(one, two, three))
# print(sametwostrings(one, two, three))