#Find the length of the longest substring in a given string.
def longestSubstring(str1):
    charSet = set()
    left = 0
    result = 0
    
    for right in range(len(str1)):
        while str1[right] in charSet:
            charSet.remove(str1[left])
            left += 1
        
        charSet.add(str1[right])
        result = max(result, right - left + 1)
    
    return result

input_str = "abcabcbb"
result = longestSubstring(input_str)
print(result)