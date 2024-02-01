def groupAnagram(strs):
    dictStr = {}
    
    for word in strs:
        sortedStr = ''.join(sorted(word))
        if sortedStr in dictStr: #sortedStr is a keyword.
            dictStr[sortedStr].append(word)
        
        else:
            dictStr[sortedStr] = [word]
            
    return list(dictStr.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))