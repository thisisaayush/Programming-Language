#Sorted List- Remove Duplicates
def removeDuplicates(nums):
    i = 0 
    for j in range(1, len(nums)):
        if nums[1] != nums[j]:
            i += 1
            nums[i] = nums [j]
            
    return i + 1

nums = [1, 1, 2, 2, 3, 4, 4, 5]
result_length = removeDuplicates(nums)
print(result_length)
print(nums[:result_length])