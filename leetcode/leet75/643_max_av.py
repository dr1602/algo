# Sliding Window

## 643. Maximum Average Subarray I

def find_max_average(nums, k):
    """
    Finds the maximum average value of a contiguous subarray of length k in the given array.

    Args:
        nums: The input integer array.
        k: The length of the subarray.

    Returns:
        The maximum average value.
    """
    M = d = 0
    for i in range(len(nums) - k):
        d = d + nums[i + k] - nums[i]
        if d > M: M = d
    return( float(sum(nums[:k])+M)/k)

