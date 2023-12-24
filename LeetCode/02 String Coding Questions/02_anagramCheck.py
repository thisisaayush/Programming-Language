#Check if two strings are Anagram or not- listen and silent are.
def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_Count = {}
    
    for char in str1:
        if char in char_Count:
            char_Count[char] += 1
        else:
            char_Count = 1
            
        
    for char in str2:
        if char in str2:
            char_Count[char] -= 1
        else:
            char_Count[char] -= 1
    
    for count in char_Count.values():
        if count != 0:
            return False
    
    return True

str1 = "listen"
str2 = "silent"

if checkAnagram(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")