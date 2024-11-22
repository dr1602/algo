# 283. Move Zeroes

Given an integer array **nums**, move all **0**'s to the end of it while maintaining the relative oreder of the non-zero elements.

**Note** that you must do this in-place withouth making a copy of the array.

## Example 1:

**Input:** nums = [0, 1, 0, 3, 12]
**Output:** [1, 3, 12, 0, 0,]

**Explanation:**

## Example 2:

**Input:** nums = [0]
**Output:** [0]

## Constraints:

* *1 <= nums.length <= 10^4*
* *-2^31 <= nums[i] <= 2^31 - 1*

**Follow up**: Could you minimize the total number of operations done?

## Intuition

I think that what we could just do, is to run on every array a single time. To do this...
We will have a pointer in position i and the other in the position i + 1
if the value first the value in i is zero and the value at i + 1, is differente to zero, we move i + 1 to i

nums = [0, 1, 0, 3, 12]
        i i+1

then:
nums = [1, 0, 0, 3, 12]
       i+1 i

the here we have a special case, in which we have two consecutive zeros....
I think that for this cases we should only validate the values, and when we find that both are zero, we just move both pointers to the next position.

then we repeat the first case
if the value first the value in i is zero and the value at i + 1, is differente to zero, we move i + 1 to i

nums = [1, 0, 0, 3, 12]
              i i+1

then:
nums = [1, 0, 3, 0, 12]
             i+1 i

Now for this to work out, we must compare again the values, so i must become i-1 and i + 1 must become i, until we find an repeat the comparission
if, the first value is zero, we switch them,
if the value in i-1 is different to zero, we stop...

this may become an error, if it doesn't find the value in i... so there could be some edge cases...
like,

1. going back as long as i - 1 is => 0, or 
2. to return the same array if the ir only 1 element inside it...

this could be of help, but, is there any other age case?

In the best scenario, the complexity could be O(1), in the worst case at least O(n), as it must run at least one team on every element.

## Algorithm

def moveZeroes(nums):

    i = 0
    z = 1

    if len(nums) == 1:
        return print(nums)

    while z < len(nums):
        if (nums[i] == 0 and nums[z] == 0) or (nums[i] != 0 and nums[z] == 0) or (nums[i] != 0 and nums[z] != 0):
            i += 1
            z += 1
        else:
            nums[i] = nums[z]
            nums[z] = 0
            if i == 0:
                i += 1
                z += 1
            else:
                i -= 1
                z -= 1
    return print(nums)

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)

nums = [0]
moveZeroes(nums)

// now looking at the algo, it has a time complexity of O(n)

// IMPROVED 

def moveZeroes(nums):
    j = 0  # Index to insert non-zero elements
    for i in range(len(nums)):
        if nums[i] != 0:
            print(f'This is nums[i]:{nums[i]}')
            print(f'This is i:{i}')
            print(f'This is j:{j}')
            nums[j], nums[i] = nums[i], nums[j]  # Swap non-zero element with current position
            j += 1
            print(f'This is preliminar nums:{nums}')
    return print(nums)

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)

nums = [0]
moveZeroes(nums)

### Approach

1. **Initialize a pointer non_zero to 0, which will keep track of the position where the next non-zero element should be placed.** This is the key, I guess..
2. Iterate through the list nums using a single loop.
3. For each non-zero element encountered, swap it with the element at the non_zero position, and then increment the non_zero pointer.
4. After the loop, all non-zero elements will be at the beginning of the list, and the non_zero pointer will be pointing to the first position where a zero was encountered.
5. The remaining positions from non_zero to the end of the list will be automatically filled with zeros since all non-zero elements have been moved to the beginning.

## Implementation

def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

### Performance
Runtime: 5 ms, Beats 73.93%
Memory:  13.13 MB, Beats 8.33%

### Code

Consider please that the comments in the code reduce its performance in time and memory, if you want to test it, I suggest you to delete them before running it in leetcode.

```

def reverseVowels(s):
    

'''
