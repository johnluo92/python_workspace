import sys
def apartmentHunting(blocks, reqs):
    # Write your code here.
    closest = dict.fromkeys(reqs, float('inf'))
    locations = [{key:float('inf') for key in reqs} for block in blocks]
        
    for i in range(len(blocks)):
        block = blocks[i]
        for key, value in block.items():
            if key in closest:
                closest[key] = i if value else closest[key]
                locations[i][key] = abs(closest[key] - i)
    
  closest = dict.fromkeys(reqs, float('inf'))
    shortestDistanceBlock = float('inf')
    bestBlock = None
    
    for i in reversed(range(len(blocks))):
        block = blocks[i]
        blockMaxDistance = float('-inf')
        for key, value in block.items():
            if key in closest:
                closest[key] = i if value else closest[key]
                locations[i][key] = min(locations[i][key], abs(closest[key] - i))
                blockMaxDistance = max(locations[i][key], blockMaxDistance)
            
        if blockMaxDistance < shortestDistanceBlock:
            shortestDistanceBlock = blockMaxDistance
            bestBlock = i
                
    for block in locations:
        print(block)
    print(bestBlock)
        
    return bestBlock