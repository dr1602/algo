# 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array **flowerbed** containing **0**'s and **1**'s, where **0** means empty and **1** means not empty, and an integer **n**, return **true** if **n** new flowers can be planted in the **flowerbed** *without violating the no-adjacent-flowers rule* and **false** otherwise.

## Example 1:

**Input:** flowerbed = [1,0,0,0,1], n = 1
**Output:** true

## Example 2:

**Input:** flowerbed = [1,0,0,0,1], n = 2
**Output:** false

## Constraints:

* *1 <= flowerbed.length <= 2 * 10^4*
* *flowerbed[i] is 0 or 1.*
* *There are no two adjacent flowers in flowerbed.*
* *0 <= n <= flowerbed.length*

## Intuition

In order to solve this problem, the first step is to understand it. The flowerbed has a minimum length of two to place the flowers, and we must consider as well the number of flowers to be placed which are "n".

A question could be, how to now if you can put the number of flowers without two touching each other?

I think it depends on the length of the array called flowerbed. And now, I must see other types of arrangements the flowerbed could have.

Ok, the problem doesn't say that the original flowers will always be in a fixed way like in this:

flowerbed = [1,0,0,0,1]

So this may add complexity to the problem, but I am almost sure that the original flowers  will not be in consecutive places, as it would crash the code without even testing it.

Let's move on to the following points.

In the case, they are always fixed at the same position as in the test, i think there should always be at least the following empty spaces:

n + 1

why? Let's make some imaginary tests:

**1. First test**

original_flowerbed = [1,0,0,0,1]
n = 1
spaces = 3
modified_flowerbed = [1,0,1,0,1]

this invalidates the exercise, the we correct the formula to n + 2 spaces

**2. Second test**

original_flowerbed = [1,0,0,0,1]
n = 2
spaces = 3
modified_flowerbed = [1,0,1,1,1]
modified_flowerbed = [1,1,1,0,1]

this test ends a failure.

**3. Third test**

original_flowerbed = [1,0,0,0,0,1]
n = 2
spaces = 4
modified_flowerbed = [1,1,1,0,0,1]
modified_flowerbed = [1,0,1,1,0,1]
modified_flowerbed = [1,0,0,1,1,1]
modified_flowerbed = [1,1,0,0,1,1]
modified_flowerbed = [1,0,1,0,1,1]

All test failed. The formula isn't n + 2.

**3. Third test**

original_flowerbed = [1,0,0,0,0,0,1]
n = 2
spaces = 5
modified_flowerbed = [1,0,1,0,1,0,1]

Success with n + 3

**4. Fourth test**

original_flowerbed = [1,0,0,0,0,0,0,0,1]
n = 3
spaces = 7
modified_flowerbed = [1,0,1,0,1,0,1,0,1]

Success with n + 4

## Algorithm

Successful formulas:

when n = 1: n + 2
when n = 2: n + 3
when n = 3: n + 4

In order to not depend on an unknown variable, let's modified it to not heavily rely on it.

it seem to be: 2n + 1

Let's test this in the succesful cases:
**1. First successful test**
n = 1
spaces = 3
formula = 2(1) + 1 = 3

**2. Second successful test**
n = 2
spaces = 5
formula = 2(2) + 1 = 5

**3s. Third successful test**
n = 3
spaces = 7
formula = 2(3) + 1 = 7

It fits well, but it heavily depends on having a flower bed with the only two initial flowers, one in the first position, and the second one in the last position. If it has a diferent configuration, the problem would require a different approach to be solved.

Still it would require knowing the empty places. To count them, it will require to look at each element, and then to count the total number of zeros.

This would require an O(n) complexity, but if it has an equal arrangement, it doesn't matter, as the the total number of empty spaces woudl be the length of the flowerbed - 2

And after testing, that isn't the case, I have to give it a second thought

## Implementation

```

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if (len(flowerbed) - 2) >= (2*n + 1):
        return True
    else:
        return False
    


        
```