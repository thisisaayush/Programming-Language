def validPalindrome(strs):
    strs = "".join(x.lower() for x in strs if x.isalnum())
    
    left = 0
    right = len(strs) - 1
    
    while left < right:
        if strs[left] != strs[right]:
            return False
        
        left += 1
        right -= 1
    
    return True


strs = "A man, a plan, a canal: Panama"
print(validPalindrome(strs))