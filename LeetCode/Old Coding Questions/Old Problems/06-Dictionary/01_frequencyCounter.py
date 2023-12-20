class FrequencyCounter:
    @staticmethod
    def frequencyCounter(str1):
        str1 = str1.split().lower()
        count = {}

        for word in str1:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        return count

word = FrequencyCounter()
print(word.frequencyCounter("Hello Everybody, this is amazing that this time we are going to deploy the last feature of the software."))