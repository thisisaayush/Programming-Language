class CharacterFrequency:
    @staticmethod
    def characterFrequency(str1):
        str1 = "".join(str1.split()).lower()
        countCharacter = {}
        for x in str1:
            if x in countCharacter:
                countCharacter[x] += 1

            else:
                countCharacter[x] = 1

        return countCharacter
