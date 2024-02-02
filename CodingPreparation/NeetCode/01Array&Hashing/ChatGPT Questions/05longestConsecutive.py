def consecutiveSequence(nums):
    numSet = set(nums)
    maxLength = 0
    
    for num in numSet:
        if num - 1 not in numSet:
            currentNum = num
            currentLength = 1
            
            while currentNum + 1 in numSet:
                currentNum +=1 
                currentLength += 1
                
        maxLength = max(currentLength, maxLength)
    
    return maxLength

nums = [100, 4, 200, 1, 3, 2]
print(consecutiveSequence(nums))