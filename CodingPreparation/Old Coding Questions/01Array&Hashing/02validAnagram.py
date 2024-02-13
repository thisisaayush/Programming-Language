#valid anagram for two strings.
def validAnagram(s, t):
    anagramDict = {}
    
    if len(s) != len(t): #if length is different, can't be anagram.
        return False
    
    for x in s:
        anagramDict[x] = anagramDict.get(x, 0) + 1
    
    for y in t:
        if y in anagramDict:
            anagramDict[y] -=1 
        else: #y character from t string is not in the dictionary.
            return False
            
    return all(value == 0 for value in anagramDict.values())

s = "eat"
t = "tea"
print(validAnagram(s, t))