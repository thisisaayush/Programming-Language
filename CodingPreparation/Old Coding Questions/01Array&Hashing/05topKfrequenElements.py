from collections import Counter

def topKelements(nums, k):
    topDict = {}
        
    for n in nums:
        topDict[n] = topDict.get(n, 0) + 1
        
    sortedDict = dict(sorted(topDict.items(), key=lambda x:x[1], reverse=True))
    
    result = [element for element, freq in list(sortedDict.items())[:k]]
    
    return result


def topKFrequent(nums, k):
    counter = Counter(nums)
    
    # sort the dictionary based on frequencies in descending order
    sorted_freq = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # extract the top k frequent elements
    result = [element for element, freq in sorted_freq[:k]]
    return result

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print("Function 1: ", topKFrequent(nums, k))


nums = [1, 1, 1, 2, 2, 3]
k = 2
print("Function 2: ",topKelements(nums, k))