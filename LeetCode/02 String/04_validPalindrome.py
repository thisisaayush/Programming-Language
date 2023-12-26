#Check if the string (word) is a Palindrome. madam == rev(madam) -> True
def palindromeCheck1(str1):
    return str1 == str1[::-1]

#Check if the string (sentence) is a Palindrome. madam == rev(madam) -> True
def palindromeCheck2(s):
    # Helper function to check if a character is alphanumeric
    def is_alphanumeric(char):
        return char.isalnum()

    # Initialize pointers
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not is_alphanumeric(s[left]):
            left += 1

        # Move right pointer to the next alphanumeric character
        while left < right and not is_alphanumeric(s[right]):
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Example usage:
print(palindromeCheck2("A man, a plan, a canal: Panama"))  # Output: True
print(palindromeCheck2("race a car"))  # Output: False
