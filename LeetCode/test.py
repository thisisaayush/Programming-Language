from operator import itemgetter

def topKFrequent(nums, k):
    # Count the frequency of each element in the array using a dictionary
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Sort the dictionary by values in descending order using itemgetter
    sorted_count = sorted(count.items(), key=itemgetter(1), reverse=True)
    
    # Extract the top k elements using a for loop
    result = []
    for key, _ in sorted_count[:k]:
        result.append(key)
    
    return result

# Example usage
nums = [1, 1, 2, 2, 3, 3, 2, 3, 1, 1, 5, 5, 5, 5, 5, 4, 4, 4, 7, 7, 7, 8, 8, 7, 7, 7, 8, 8]
k = 2
result = topKFrequent(nums, k)
print(result)
