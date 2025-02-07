# Sliding Window

## 1493. Longest Subarray of 1's After Deleting One Element

Given a binary array **nums**, you should delete one element from it.

Return *the size of the longest non-empty subarray containing only* **1**'s *in the resulting array*. Return **0** if there is no such subarray.

### Example 1:

**Input:** nums = [1,1,0,1]
**Output:** 3
**Explanation:** After deleting the number in the position 2, [1,1,1] contians in 3 numbers with value of 1's.

### Example 2:

**Input:** nums = [0,1,1,1,0,1,1,0,1]
**Output:** 5
**Explanation:** After deleting the number in the position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

### Example 3:

**Input:** nums = [1,1,1]
**Output:** 2
**Explanation:** You must delete one element.

### Constraints:

*1 <= nums.length <= 10^5*
*nums[1] is either 0 or 1*

## Algorithm

```py

def longestSubarray(nums):
    max_count = 0
    count_ones = 0
    zeros = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        count_ones = right - left + 1 - zeros
        max_count = max(max_count, count_ones)
    
    if zeros == 0:
        max_count = len(nums) - 1

    return max_count

```

## Complexity

Runtime: 111ms Beats 8.64%
Memory: 16.92 MB Beats 17.77%
