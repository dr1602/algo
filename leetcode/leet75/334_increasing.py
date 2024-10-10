# 334. Increasing Triplet Subsequence

'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
a. 1 <= nums.length <= 5 * 10**5
b. -231 <= nums[i] <= 231 - 1

Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

    
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# Proposed solution

'''
I think it can be something like a sliding window, in which with two pointers I check the value of two contiguos values.

1. I create the pointer left which is in the position 0
2. I create the pointer right which is in the position 1
3. Compare the left with right
4. If left is smaller than right, we simple move right to do the comparission
5. If left is bigger than right then we move both vulues:
    .... we move left to right
    .... and we move right to right + 1
6. We keep on the process until we either
    .... find the triplets and return true
    .... finish the array with no triplets and return false

I guess the complexity is O(logn)

def increasingTriplet(nums):
    left = 0
    right = 1

    flag = left - right

    for num in nums:
        if flag == 3:
            return True

        if right > len(nums):
            return False

        if nums[left] < nums[right]:
            right += 1
        else:
            left = right
            right += 1
            if right > len(nums):
                return False
    
    return False

'''

# Ayuda


'''
def increasingTriplet(nums):
    left = 0
    right = 1

    for num in nums:
        if right >= len(nums): # Check before comparison
            return False
        if left < right and nums[left] < nums[right]:
            return True
        elif nums[left] > num:
            left = right
        right += 1
    
    return False

'''

def increasingTriplet(nums):
    left = 0
    right = 1

    for num in nums:
        if right >= len(nums): # Check before comparison
            return False
        if left < right and nums[left] < nums[right]:
            return True
        elif nums[left] > num:
            left = right
        right += 1
    
    return False

if __name__ == '__main__':
    nums_1 = [1,2,3,4,5]
    nums_2 = [5,4,3,2,1]
    nums_3 = [2,1,5,0,4,6]

result_1 = increasingTriplet(nums_1)
result_2 = increasingTriplet(nums_2)
result_3 = increasingTriplet(nums_3)

print(result_1)
print(result_2)
print(result_3)

'''
def increasingTriplet(nums):
    left = 0
    right = 1

    flag = left - right

    for num in nums:
        if flag == 3:
            return True

        if right > len(nums):
            return False

        if nums[left] < nums[right]:
            right += 1
        else:
            left = right
            right += 1
            if right > len(nums):
                return False
    
    return False

if __name__ == '__main__':
    nums_1 = [1,2,3,4,5]
    nums_2 = [5,4,3,2,1]
    nums_3 = [2,1,5,0,4,6]

result_1 = increasingTriplet(nums_1)
result_2 = increasingTriplet(nums_2)
result_3 = increasingTriplet(nums_3)

print(nums_1)
print(nums_2)
print(nums_3)

# Result:
Traceback (most recent call last):
  File "/root/algo/leetcode/leet75/334_increasing.py", line 109, in <module>
    result_1 = increasingTriplet(nums_1)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/algo/leetcode/leet75/334_increasing.py", line 94, in increasingTriplet
    if nums[left] < nums[right]:
                    ~~~~^^^^^^^
IndexError: list index out of range
'''