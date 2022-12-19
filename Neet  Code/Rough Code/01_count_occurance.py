def my_solutions(nums: list[int], k):
    count = {}

    for n in nums:
        count[n] = 1 + count.get(n,0)

    freq = [[] for i in range(len(nums))]

    for key, value in count.items():
        freq[value].append(key)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(my_solutions([1,2,1,3,2,1], 2))