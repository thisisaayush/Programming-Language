def binarySearch(array, target):
    
    left = 0
    right = len(array) - 1
    
    while left <= right:
        midValue = (left + right) // 2
        
        if array[midValue] == target:
            return midValue
        
        elif array[midValue] > target:
            right = midValue - 1
        
        else:
            left = midValue + 1
        
    return "Value Not Found!"

num = [1,4,6,8,9]
print(binarySearch(num, 9))
    