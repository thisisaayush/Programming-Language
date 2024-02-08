def smallestSubarraySum(nums,s):
    minLen = float('inf')
    start = 0
    cSum = 0
    
    for end, n in enumerate(nums):
        cSum += n
        
        while cSum >= s:
            minLen = min(minLen, end - start + 1)
            cSum -= nums[start]
            start += 1
        
    if minLen == float('inf'):
        return 0
        
    else:
        return minLen

s = 7
nums = [2, 3, 1, 2, 4, 3]
output = smallestSubarraySum(nums, s)
print(output) 