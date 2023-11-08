class NonRepeatChar:
    @staticmethod
    def nonRepeatChar(str1):
        charCount = {}

        for char in str1:
            if char in charCount:
                charCount[char] += 1

            else:
                charCount[char] = 1

        for char in str1:
            if charCount[char] == 1:
                return char

        return None

test = NonRepeatChar()
print(test.nonRepeatChar("hello world"))