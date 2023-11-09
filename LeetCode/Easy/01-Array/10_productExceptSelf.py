def product_except_self(nums):
    product = 1
    output = []

    for num in nums:
        output.append(product)
        product *= num

    product = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= product
        product *= nums[i]

    return output

print(product_except_self([1,2,3,4,5]))