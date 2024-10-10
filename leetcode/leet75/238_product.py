# 238. Product of array except self

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constrains:

a. You must write an algorithm that runs in O(n) time and without using the division operation.
b. 2 <= nums.length <= 105
c. -30 <= nums[i] <= 30
d. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n # Initilize the result array with 1

        # Step 1: Compute the left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i] # update the left product for the next iteration

        # Step 2: Compute the right products and update the result array.
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product # Multiply by the right product
            right_product *= nums[i] # Update the right product for the next iteration

        return result

        

# Persona Solution

'''

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

24  12   8   6 
comes from multiplying
2    1   1   1
3    3   2   2
4    4   4   3

1. check every position on arr
2. Delete from that array the current item -> this would require a copy of the array
3. then store the result in the position of the current item -> that would require another array
4. then return the final array

---- this would require running over the array only 1 time
---- maybe, it wouldn't need two arrays, just one
'''

'''
def productExceptSelfTest(nums):

    new_array=[]

    for index, num in nums:
        


'''

'''
Just to multiply, I realized that I would need another cicle, which would make the complexity from n to n square.

there is another method, which is not a division that I can use,

every number ^ -1 = 1/number, so instead of using a division, it would be enought to multiply it by their negative

but, still the reaming problem could be how to multiply the elements with generating another cicle

1. In the position n, I take the value of n
2. I raise the number in n to minus 1
3. I multiply all the numbers in the array
4. store the result in a new array in the position of n
5.  repeat the process until you go through all the elements of the array

def test(nums):

    new_nums=[]
    result=1

    for index, num in enumerate(nums):
        if nums[index] == 0:
            new_nums.append(0)
        else:
            nums[index] = num ** -1
            result *= num
            new_nums.append(result)

    return new_nums

if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    result = test(nums)

    print(result)

        
            

'''

def test(nums):

    new_nums=[]
    result=1

    for index, num in enumerate(nums):
        if nums[index] == 0:
            new_nums.append(0)
        else:
            nums[index] = num ** -1
            result *= num
            new_nums.append(result)

    return new_nums

if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    result = test(nums)

    print(result)

# Another solution:

def alternative(nums):
    output = [1] * len(nums)

    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output


print([1] * 3)
# [1, 1, 1]

print(range(len([1] * 3)))
# range(0, 3)
        