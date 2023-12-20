def twoSumTarget(self, nums: list, target: int) -> list:
    preMap = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in preMap:
            return [preMap[diff], index]
        
        preMap[value] = index
    
    return
        
