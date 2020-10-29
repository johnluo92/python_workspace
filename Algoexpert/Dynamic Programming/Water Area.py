'''Water Area

You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width 1. Imagine water being poured over all of the pillars.

Write a function that returns the surface area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored.
'''

def waterArea(heights):
    # Write your code here.
	if heights == [] :
		return 0
    water = [None for x in heights]
    leftMax = [None for x in heights]
    leftMax[0] = 0
    rightMax = [None for x in heights]
    rightMax[-1] = 0
    curmax = heights[0]
    
    for i in range(1, len(heights)):
        curmax = max(heights[i], curmax)
        leftMax[i] = curmax
    print(leftMax)
        
    curmax = heights[-1]
    
    for i in reversed(range(len(heights)-1)):
        curmax = max(heights[i+1], curmax)
        rightMax[i] = curmax
    print(rightMax)
    
    for i in range(len(water)):
        minHeight = min(leftMax[i],rightMax[i])
        if heights[i] < minHeight:
            water[i] = minHeight - heights[i]
        else:
            water[i] = 0
            
    return sum(water)


heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

print(waterArea(heights)) # True