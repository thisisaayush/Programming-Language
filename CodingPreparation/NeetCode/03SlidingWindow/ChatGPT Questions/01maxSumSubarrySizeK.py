def maxSumSubArraySize(nums, k):
    maxSum = float('-inf')
    cSum = 0
    
    for i in range(len(nums)):
        cSum += nums[i]
        
        if i >= k - 1:
            maxSum = max(maxSum, cSum)
            cSum -= nums[i - k + 1]
    
    return maxSum

nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
output = maxSumSubArraySize(nums, k)
print(output)