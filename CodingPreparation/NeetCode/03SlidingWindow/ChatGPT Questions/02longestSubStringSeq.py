def longestSubStringSeq(strs):
    seen = set()
    maxLen = 0
    start = 0
    
    for end, str in enumerate(strs):
        if str in seen:
            seen.remove(strs[start])
            start += 1
        
        seen.add(str)
        maxLen = max(maxLen, end - start + 1)
    
    return maxLen

s = "abcabdcbb"
output = longestSubStringSeq(s)
print(output)  # Output: 3
        