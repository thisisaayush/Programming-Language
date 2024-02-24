def maxRight(nums):
    maxR = 0
    j = 1
    
    for i in range(len(nums)):
        while j < len(nums):
            maxR = max(maxR, nums[j + i])
            j += 1
        
        nums[i] = maxR
        maxR = 0
        j = 1
        
        if i == len(nums) - 1:
            nums[i] = -1
    
    return nums