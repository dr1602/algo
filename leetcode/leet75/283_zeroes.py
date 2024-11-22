
'''
TEST:

nums = [0, 1, 0, 3, 12]

i = 0

while i < len(nums):
    
    print(i)
    print(nums[i])
    i += 1
'''

def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)

nums = [0]
moveZeroes(nums)