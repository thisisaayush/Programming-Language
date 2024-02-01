def trappingRainWater(heights):
    if not heights:
        return 0
    
    left = 0
    right = len(heights) - 1
    leftMax = heights[left]
    rightMax = heights[right]
    
    result = 0
    
    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, heights[left])
            result += leftMax - heights[left]
        
        else:
            right -= 1
            rightMax = max(rightMax, heights[right])
            result += rightMax - heights[right]
            
    return result
            