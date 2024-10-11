# Two Pointers

## 1679. Max Number of K-Sum Pairs

You are given an integer array **nums** and an integer **k**.

In one operation, you can pick two numbers from the array whose sum equals **k** and remove them from the array.

Return *the maximum number of operations you can perform on the array.*

Example 1:

**Input:** nums = [1,2,3,4], k = 5
**Output:** 2
**Explanation:** Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []

There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

**Input:** nums = [3,1,3,4,3], k = 6
**Output:** 1
**Explanation:** Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]

There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
a. *1 <= nums.length <= 105*
b. *1 <= nums[i] <= 109*
c. *1 <= k <= 109*

### Possible solution

[1,2,3,4]

1. Compare the initial element with  i + 1 (but this comparison can be made backwards)
2. I validate if the sum of the comparison is equals to 5
3. If they are both numbers are deleted from the array.
4. if both values were deleted there is no need to move the pointers
5. if not, we move the right pointer.

as for what the second example says, it seem that we move the pointers starting from the left.

it is not specified if the array is arranged.


```md

def maxOperations(nums, k):
    left = 0
    right = 1
    count = 0

    while left < len(nums) - 1:
        if right < len(nums):
            if nums[left] + nums[right] == k:
                nums.pop(right)
                nums.pop(left)
                count += 1
                right = left + 1
            else:
                right += 1
        else: 
            left += 1
            right = left + 1

    return count

```