class NonRepeatChar:
    @staticmethod
    def nonRepeatChar(str1):
        charCount = {}
        str1 = "".join(str1.split()).lower()

        for char in str1:
            if char in charCount: #value char comparing to charCount Key
                charCount[char] += 1

            else:
                charCount[char] = 1

        for char in str1:
            if charCount[char] == 1:
                return char

        return None

test = NonRepeatChar()
print(test.nonRepeatChar("hello world"))