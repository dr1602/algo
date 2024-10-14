# Sliding Window

# 1004. Max Consecutive Ones III

def longestOnes(nums, k):
    left = 0
    right = 0
    zeros = 0
    max_length = 0

    while right < len(nums):
        if nums[right] == 0:
            zeros += 1
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length