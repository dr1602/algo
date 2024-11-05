# 605. Can Place Flowers

**This requires a greedy aproach**

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

### Intuition 2

This approach didn't work but I believe that the key is to have at least 3 consecutive 0s in order to be able to work with this Algorithm.

So we can use again this to test the idea:

**1. First test**

original_flowerbed = [1,0,0,0,1]

* Process:

[1,0,0,0,1]

First I must check the first value:
If it is a 1 - I move to the next value with my counter as a zeros..
If it is a 0 - I check the next value if it is a zaero..

In the secoind iteration, we check the value:
If it is a 1 - I move to the next value with my counter as a zeros..
If it is a 0 - I check the next value if it is a zaero..

Ok, here I get an idea...
The space between 2 ones, most be at least of three zeros.. so we can actually use the index as a reference...

if the distance between 1 is 3, it may be a fit <- this value instead of being a fixed one, it could be a formula, the formula I providedad with an sliding window. Maybe
if it is not, it may not be a fit...

From this I am thinking that, no matter the arrangement, there are only to possibilities to be true result:
1. If they are consecutive zeros, the amount of zeros must be at least 2n + 1
2. If the they are not consecutive zeros, the space between zeros must be at least 3. And this groups of 3 must be repeated n times.

So from here we can also get some conclusions
1. If the array is smaller in length than 2n + 1
or
2. If the array is smaller in length than 3n.

Then, the case is false, the flowers cannot be planted...

So this can reduce the number of iterations to even zero.

In the other hand you must count.



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

### Algorithm 2

From the *second Intuition* we can get some variables.

white_spaces

length (which is not a variable)


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

## Implementation 2

```

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """

    # Base case
    if len(flowerbed) < (2*n + 1):
        return False

    # Other cases
    for i, flower in enumerate(flowerbed):
        white_spaces = 0

        if len(flowerbed) - i < (2*n + 1) and white_spaces < 3 and len(flowerbed) < (white_spaces - (2*n + 1)) :
            return False
        elif white_spaces >= (2*n + 1):
            return True
        elif flower == 0:
            white_spaces += 1
        elif flower == 1:
            if white_spaces < 3:
                white_spaces = 0
            else:
                continue

    return False

```

## test

**1. First test**

original_flowerbed = [1,0,0,0,1]
n = 1

5 < 3 ? False, continues

1. 
5 - 0 < 3 ? False and 0 < 3: True: False
0 => 3 ? False
1 == 0 ? False
0 == 0 ? True

2. 
5 - 1 < 3 ? False and 1 < 3: True: False
0 => 3 ? False
0 == 0 ? True

3. 
5 - 2 < 3 ? True and 0 < 3: True: True that returns False

complexity of O(n) in memory and time 



**2. Second test**

original_flowerbed = [1,1,0,0,1]
n = 2

5 < 3 ? False, continues

1. 
5 - 0 < 3 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? False
0 == 0 ? True

3. 
5 - 1 < 3 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? False
0 == 0 ? True

1. 
5 - 2 < 3 ? True and 0 < True: True that returns False

**3. Third test**

original_flowerbed = [1,0,0,1,0,1]
n = 2

6 < 3 ? False, continues

1. 
6 - 0 < 5 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? False
0 == 0 ? True

2. 
6 - 1 < 5 ? False and 1 < 5: True: False
1 => 5 ? False
0 == 0 ? True

3. 
6 - 2 < 5 ? True and 2 < 5: True: True that returns False

**4. Fourth test**

original_flowerbed = [1,0,0,0,1,0,0,1]
n = 2

8 < 5 ? False, continues

1. 
8 - 0 < 5 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? False
0 == 0 ? True

2. 
8 - 1 < 5 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? True

3. 
8 - 2 < 5 ? False and 1 < 5: True: False
1 => 5 ? False
1 == 0 ? True

3. 
8 - 3 < 5 ? False and 2 < 5: True: False
2 => 5 ? False
1 == 0 ? True

4. 
8 - 4 < 5 ? True and 3 < 5: True: True that returns False

**5. Fifth test**

original_flowerbed = [1,0,0,0,1,0,0,0,1]
n = 2

9 < 5 ? False, continues

1. 
9 - 0 < 5 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? False
0 == 0 ? True

2. 
9 - 1 < 5 ? False and 0 < 5: True: False
0 => 5 ? False
1 == 0 ? True

3. 
9 - 2 < 5 ? False and 1 < 5: True: False
1 => 5 ? False
1 == 0 ? True

3. 
9 - 3 < 5 ? False and 2 < 5: True: False
2 => 5 ? False
1 == 0 ? True

4. 
9 - 4 < 5 ? False and 3 < 5: True: False
3 => 5 ? False
1 == 0 ? True

5. 
9 - 5 < 5 ? True and 4 < 5: True: True that returns False

## Proposed Solution A

**Iterate over the flowerbed**
* Check if the current plot is empty(O)
* If the current plot is empty and the prevoious and next plat are also empty we can plant a flower in increment the n counter.
* Move to the next plot

**Iterate over the flowerbed**
* If n becomes O, it means we've succesfully planted all the flowers
* Otherwise, we haven't planted enough flowers

**Failed**

```py

def canPlaceFlowers( flowerbed: List[int], n: int) -> bool:
    count = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 0
            count += 1
            if count >= n:
                return True
    
    return False

## it doesnt pass all tests
```

## Proposed Solution B

**This Solution worked**

``` py

def canPlaceFlowers( flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True
    
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        
    return False
```

Runtime: 14ms Beats 26.38%
Memory: 12.28MB Beats 55.05%

## Proposed Solution C

**This Solution worked**

``` py

def canPlaceFlowers( flowerbed: List[int], n: int) -> bool:
    # Solver for edge case in which there is a an array with a single 0
    if flowerbed == [0]:
        return True

    # Test for an edge case in which the first two values are 0, and then plants there
    put_flower = 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        put_flower += 1

    # Tests for and edge case in which the last two values are 0, and then plants there
    if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0:
        flowerbed[len(flowerbed) - 1] = 1
        put_flower += 1

    # Tests if it is possible to plant in in between values from the value in the positions
    # 1 (in which 0 is the first element) and len(arr) - 1 (which is the item before the last one.)
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            put_flower += 1
            # if all spaces are empy, you can plant there
            if put_flower >= n:
                return True

    # If all the plants where planted, then you achieved the goal and it was set as true
    if put_flower >= n:
        return True

    # If non of this is met, it return false
    return False

```

Runtime: 8ms Beats 67%
Memory: 12.30MB Beats 29.92%

## Proposed Solution C

The same code without comments.

``` py

def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if flowerbed == [0]:
        return True

    put_flower = 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        put_flower += 1

    if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0:
        flowerbed[len(flowerbed) - 1] = 1
        put_flower += 1

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            put_flower += 1
            if put_flower >= n:
                # print("put_flower: %s | n: %s | statement: %s" % (put_flower, n, put_flower >= n))
                return True

    if put_flower >= n:
        return True

    return False

```

Runtime: 3ms Beats 96.65%
Memory: 12.30MB Beats 29.92%
