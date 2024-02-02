from collections import Counter

def CountAngramPattern(strs, pattern):
    pattern_Counter = Counter(pattern)
    current_Counter = Counter()
    result = []
    
    for end in range(len(strs)):
        current_Counter[strs[end]] += 1
        
        if end >= len(pattern) - 1:
            if current_Counter == pattern_Counter:
                result.append(end - len(pattern) + 1)
            
            current_Counter[strs[end - len(pattern) + 1]] -= 1
            if  current_Counter[strs[end - len(pattern) + 1]] == 0:
                del  current_Counter[strs[end - len(pattern) + 1]]
            
    
    return result
                
s = "cbaebabacd"
p = "abc"
print(CountAngramPattern(s,p))