# Max water in a container of given heights.
def maxWater(array):
    left = 0
    right = len(array) - 1
    max_area = 0
    
    while left < right:
        height = min(array[left], array[right])
        width = right - left
        max_area = max(max_area, height * width)
        
        if array[left] < array[right]:
            left += 1
        else: 
            right -= 1
        
    return max_area