class CommonFrequency:
    @staticmethod
    def commonFrequency(list1, list2):
        countlist1 = {}
        for x in list1:
            if x in countlist1:
                countlist1[x] += 1
            else:
                countlist1[x] = 1

        commonFrequency = {}

        for x in list2:
            if x in countlist1 and x not in commonFrequency:
                commonFrequency[x] = countlist1[x]
            elif x in countlist1 and x in commonFrequency:
                commonFrequency[x] += 1

        return commonFrequency

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 4, 5]
result = CommonFrequency()
x = result.commonFrequency(list1, list2)

print(x)