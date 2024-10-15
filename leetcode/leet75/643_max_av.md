# Sliding Window

# Look for more optimal solutions

## 643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

### Example 1:

**Input:** nums = [1,12,-5,-6,50,3], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

### Example 2:

**Input:** nums = [5], k = 1
**Output:** 5.00000

### Constraints:

* *n == nums.length*
* *1 <= k <= n <= 105*
* *-104 <= nums[i] <= 104*

```
def find_max_average(nums, k):
    """
    Finds the maximum average value of a contiguous subarray of length k in the given array.

    Args:
        nums: The input integer array.
        k: The length of the subarray.

    Returns:
        The maximum average value.
    """

    if len(nums) < k:
        return 0 # Handle edge case: k is greater than the array length

    # Calculate the sum of the first k elements
    for i in range (k, len(nums)):
        window_sum = sum(nums[:k])
        average = window_sum / k
        max_average = max(max_average, average)

    return max_average

```