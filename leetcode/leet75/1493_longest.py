def longestSubarray(nums):
    max_count = 0
    count_ones = 0
    zeros = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # Shrink window if there are more tha one zero
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Update count of ones in current window
        count_ones = right - left + 1 - zeros
        max_count = max(max_count, count_ones)
    
    # If there are no zeros in the array, we must delete one element to comply with the problem's constraint
    if zeros == 0:
        max_count = len(nums) - 1

    return max_count

# Run test
if __name__ == '__main__':
    a=[1,1,0,1]
    b=[0,1,1,1,0,1,1,0,1]
    c=[1,1,1]

    result_a = longestSubarray(a)
    result_b = longestSubarray(b)
    result_c = longestSubarray(c)

    print(result_a) # Output: 3
    print(result_b) # Output: 5
    print(result_c) # Output: 3