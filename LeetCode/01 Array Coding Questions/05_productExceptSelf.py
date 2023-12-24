#Find the product in an nums array such that output[i] is equal to the product of all the elements of nums except nums[i]. 
def productExceptSelf(nums):
    results = [1] * len(nums) #results is a new array.
    
    prefix = 1
    for i in range(len(nums)):
        results[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        results[i] *= postfix
        postfix *= nums[i]