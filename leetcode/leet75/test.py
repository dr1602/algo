from functools import reduce

def multiply_elements(nums):
    return reduce(lambda x, y: x * y, nums, 1)

nums = [1, 2, 3, 4]
product = multiply_elements(nums)
print(product)  # Output: 24