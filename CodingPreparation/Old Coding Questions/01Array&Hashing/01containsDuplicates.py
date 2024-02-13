#unsorted array.
def containsDuplicates(nums):
    seen = set()
    
    for n in nums:
        if n in seen:
            return True #means contains duplicates.
        
        seen.add(n)
    
    return False #means doesn't contain duplicates.

nums = [1,2,3,1]
print(containsDuplicates(nums))