def maxSubarray(nums, k):
    maxSum = 0

    
    for i in range(len(nums)):
        currSum += nums[i]
        
        if i >= k - 1:
            maxSum = max(maxSum, currSum)
            currSum -= nums[i - k + 1]
            
    
    return maxSum

nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
output = maxSubarray(nums, k)
print(output)