def targetSumIndices(arr, target):
    indices = {}

    for i, num in enumerate(arr):
        diff = target - num

        if diff in indices:
            return [indices[diff], i]

        indices[num] = i

    return None

print(targetSumIndices([1,4,5,6,8,3], 13))