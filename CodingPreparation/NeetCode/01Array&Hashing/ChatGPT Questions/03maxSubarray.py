def maxSubarray(nums):
    maxSum = float('-inf')
    currentSum = 0
    
    for num in nums:
        currentSum = max(num, currentSum + num)
        maxSum = max(maxSum, currentSum)
        
    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(nums))