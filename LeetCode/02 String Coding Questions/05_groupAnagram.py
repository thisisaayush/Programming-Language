#list of word is give, group the anagram words in a list.
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
