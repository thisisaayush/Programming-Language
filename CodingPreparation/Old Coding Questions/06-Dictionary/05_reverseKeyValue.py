class ReverseKeyValue:
    @staticmethod
    def reverseKeyValue(dict1):
        reverseDict = {}
        for key, value in dict1.items():
            reverseDict[value] = key

        return reverseDict

x = ReverseKeyValue()
print(x.reverseKeyValue({'a': 1, 'b': 2, 'c': 3}))