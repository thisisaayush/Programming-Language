def maxElement(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

print(maxElement([4,2,1,5,7,8,6]))