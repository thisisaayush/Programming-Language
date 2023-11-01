def findMissingNumber(nums):
    n = len(nums)
    total_sum = (n * (n + 1)) // 2 # mathematical formula for calculating the sum of the first n numbers starting from 0.
    actual_sum = sum(nums)
    return total_sum - actual_sum

arr = [0, 1,2,3,4,5,6,8,9] # 7 is missing
print(findMissingNumber(arr))

