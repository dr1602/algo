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

