#unsorted array- return indices.
#nums = [2,8,9,6,5], target = 11
def twoSum(nums, target):
    targetDict = {}
    
    for i, n in enumerate(nums):
        difference = target - n
        
        if difference in targetDict:
            return[i, targetDict[difference]]
    
        targetDict[n] = i
    
nums = [1,2,6,7,4,5,3,8]
target = 9
print(twoSum(nums, target))

