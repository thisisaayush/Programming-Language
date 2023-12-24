#Remove Duplicates from Unsorted Array.
def removeDuplicates(nums):
    seen = set()
    
    for n in nums: 
        if n not in seen:
            seen.add(n)
    
    return list(seen)

nums = [4, 2, 8, 5, 2, 7, 6, 1, 4]
result = removeDuplicates(nums)
print(result)