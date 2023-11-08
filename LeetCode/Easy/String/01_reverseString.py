class ReverseString:
    @staticmethod
    def reverseString1(str1):
        revString = ""

        for i in range(len(str1)-1, -1, -1):
            revString += str1[i]

        return revString

    @staticmethod
    def reverseString2(str1):
        return str1[::-1]


test = ReverseString()
print(test.reverseString1("hello 1 world"))
print(test.reverseString2("hello 1 world"))