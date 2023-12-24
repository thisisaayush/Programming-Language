class PalindromeCheck:
    @staticmethod
    def checkPalindrome1(str1):
        str2 = "".join(str1.split()).lower()
        return str2[::-1] == str2

    @staticmethod
    def checkPalindrome2(str1):
        str2 = "".join(str1.split()).lower()
        left, right = 0, len(str1) - 1

        while left < right:
            if str2[left] != str2[right]:
                return False

            else:
                left += 1
                right -= 1

        return True

test = PalindromeCheck()
print(test.checkPalindrome1("m ,a da m"))
print(test.checkPalindrome1("m a d a m"))

