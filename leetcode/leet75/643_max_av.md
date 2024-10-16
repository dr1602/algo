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

```py
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

### Provided answer

```py
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
    window_sum = float(sum(nums[:k]))
    max_average = float(window_sum / k)
    
    # Slide the window and update the sum and average
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        average = float(window_sum / k)
        max_average = max(max_average, average)

    return max_average
```

### Optimal in time

It beats:
885ms Beats 92.52% in runtime
21.15 MB Beats 36.20% in memory

```
def findMaxAverage(nums: List[int], k: int) -> float:
    M = d = 0
    for i in range(len(nums) - k):
        d += nums[i + k] - nums[i]
        if d > M: M = d
    return(float(sum(nums[:k])+M)/k)
```

### Optimal in memory
It beats:
903ms Beats 78.08% in runtime
20.89 MB Beats 97.40% in memory

```
def find_max_average(nums, k):
    M = d = 0
    for i in range(len(nums) - k):
        d = d + nums[i + k] - nums[i]
        if d > M: M = d
    return( float(sum(nums[:k])+M)/k)
```

### Most optimal solution:

```
def find_max_average(nums, k):
    curr_sum = sum(nums[:k])
    for i in xrange(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return float(max_sum)/k

```