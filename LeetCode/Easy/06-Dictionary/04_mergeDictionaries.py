class MergeDictionaries:
    @staticmethod
    def mergeDictionaries(dict1, dict2):
        mergeDict = {}

        for x in dict1:
            if x in dict2:
                mergeDict[x] = dict1[x] + dict2[x]

            else:
                mergeDict[x] = dict1[x]

        for x in dict2:
            if x not in dict1:
                mergeDict[x] = dict2[x]

        return mergeDict

dict1 = {'a': 1, 'b': 2, 'c': 3, 'e' : 6}
dict2 = {'b': 3, 'c': 4, 'd': 5, 'f' : 5}

result = MergeDictionaries.mergeDictionaries(dict1, dict2)
print(result)