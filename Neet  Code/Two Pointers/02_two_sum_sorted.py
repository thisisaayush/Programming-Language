def twoSum(nums: list, target):
    l,r = 0, len(nums) - 1

    while l < r:
        curSum = nums[l] + nums[r]

        if curSum < target:
            l += 1
        if curSum > target:
            r -= 1
        else:
            return [l + 1, r + 1]