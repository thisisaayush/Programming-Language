def longestConqSeq(nums):
    seen = set(nums)
    maxLen = float('-inf')
    
    for n in nums:
        if n - 1 not in seen:
            countLen = 0
            while (n + countLen) in seen:
                countLen +=1
        
            maxLen = max(maxLen, countLen)
    
    return maxLen

nums = [100,4,200,1,3,2]
print(longestConqSeq(nums))
            