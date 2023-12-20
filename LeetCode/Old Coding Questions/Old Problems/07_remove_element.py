def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return nums

print(removeElement([1,2,1,2,3,5,4,6,7,7,3,4,9], 7))