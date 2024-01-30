def twoSum(nums, target):
    dictNum = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in dictNum:
            return [dictNum[diff], i]

        dictNum[num] = i
        
nums = [2, 7, 11, 15]
target = 13
print(twoSum(nums, target))