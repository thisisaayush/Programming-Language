class CountLetters:
    @staticmethod
    def countLetters(str1):
        str1 = "".join(str1.split()).lower()
        countLetters = {}

        for char in str1:
            if char in countLetters:
                countLetters[char] += 1

            else:
                countLetters[char] = 1

        return countLetters

char = CountLetters()
print("Number of characters: ", char.countLetters("Hello this is ammazing"))
