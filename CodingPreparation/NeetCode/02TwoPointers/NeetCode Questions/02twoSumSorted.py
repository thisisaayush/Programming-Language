def twoSumSorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        cSum = nums[left] + nums[right]
        
        if cSum == target:
            return [left, right]
        
        elif cSum > target:
            right -= 1
        
        else:
            left += 1
    
    return 'None'
        
nums = [2,7,11,15]
print(twoSumSorted(nums, 9))
    