class CountVowels:
    @staticmethod
    def countVowels(str1):
        vowels = 'aeiou'
        countVowel = {x: 0 for x in vowels}

        str1 = "".join(str1.split()).lower()

        for x in str1:
            if x in vowels:
                countVowel[x] += 1

        print("Total Vowels: ", countVowel)

vowel = CountVowels()
print(vowel.countVowels('hello world this is amazing'))
