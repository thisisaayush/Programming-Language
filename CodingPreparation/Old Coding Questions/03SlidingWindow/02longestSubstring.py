def longestSubstring(strs):
    setSeen = set()
    start = 0
    maxLen = 0
    
    for end in range(len(strs)):
        while strs[end] in setSeen:
            setSeen.remove(strs[end])
            start += 1
        
        setSeen.add(strs[end])
        maxLen = max(maxLen, end - start + 1)
        
    return maxLen

strs = "abcabcbb"
print(longestSubstring(strs))
            