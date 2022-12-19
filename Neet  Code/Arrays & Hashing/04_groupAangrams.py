import collections

def groupAnagram(array: list[str]) -> list[list[str]]:
    default_list = collections.defaultdict(list)

    for str in array:
        count = [0] * 26
        for l in str:
            count[ord(l) - ord('a')] += 1

        default_list[tuple(count)].append(str)

    return default_list.values()

array = ['tea','eat','naru','nuar','tachii','sasuke']
print(groupAnagram(array))