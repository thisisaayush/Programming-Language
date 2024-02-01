def mostWater(heights):
    maxWater = 0
    left = 0
    right = len(heights) - 1
    
    while left < right:
        width = right - left
        
        area = min(heights[left], heights[right]) * width
        maxWater = max(area, maxWater)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
        
    return maxWater


height = [1,8,6,2,5,4,8,3,7]
print(mostWater(height))