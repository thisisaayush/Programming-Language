def concatArray(nums):
    ans = [0] * len(nums)
    
    for i in range (len(ans)):
        j = 0
        
        if i < len(nums):
            ans[i] = nums[i]
        else:
            ans[i] = nums[j]
            j += 1
        
    return ans