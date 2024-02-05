#group all the anagram as a list.
def groupAnagram(strs):
    anagramDict = {}
    
    for word in strs:
        sortedWord = "".join(sorted(word))
        
        if sortedWord in anagramDict: #sortedWord is a key and checking if it is already in anagramDict or not.
            anagramDict[sortedWord].append(word)
        
        else:
            anagramDict[sortedWord] = [word]
        
    return list(anagramDict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))