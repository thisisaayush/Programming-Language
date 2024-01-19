def find_unique_element(arr):
    element_count = {}
    
    # Count occurrences of each element in the array
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1
    
    # Find the element with count 1
    for element, count in element_count.items():
        if count == 1:
            return element

# Example usage:
arr = [2, 4, 7, 2, 4]
unique_element = find_unique_element(arr)
print(f"The unique element is: {unique_element}")
