# Two Pointers

## 1679. Max Number of K-Sum Pairs

def maxOperations(nums, k):
    freq = {}
    operations = 0

    for num in nums:
        complement = k - num
        if complement in freq and freq[complement] > 0:
            # A pair is found
            operations += 1
            # Decrease ht frequency of the complement
            freq[complement] -= 1
        else:
            # Increment the frequency of the current number
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    
    return operations