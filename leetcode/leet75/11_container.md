# Two Pointers

## 11. Container with most water

You are given an integer array **height** of length **n**. There are **n** vertical lines drawn such that the two endpoints of the i^th line are *(i, 0)* and *(i, height[i])*.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

### Example 1:

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:

**Input:** height = [1,1]
**Output:** 1

### Constraints
a. *n == height.length*
b. *2 <= n <= 105*
c. *0 <= height[i] <= 104*

### My proposal

Lets have this as an example:
[1,8,6,2,5,4,8,3,7]

we can have 2 pointers, left and right:
left = 0
right = 1

because we need at least 2 pointers in different positions to make a container

then at the beginning
we have left at 1 and right at 8 thus the area is 1 as it cannot slant
we most keep this area in memory so we can compare it

*** what maters is the area, no the position of the area
*** cannot slant
*** we advance right as long as right is in a position lower than len of ar

as arr[left] < arr[right], we move left to right, as there this increase the chances to get a bigger area.

we advance right + 1

we have that

arr[left or 1] = 8
arr[right or 2] = 6

the area is determined by:
a. the lowest vertical line
b. the space between left and right

so

area = 6 * 6 * (right - left)

and if this space is larger than the previous area,it stored

while the right hasnt rich the area we continue.

as the value in left is larger than the value in right we move right one value...

and we can continue this until we get the answer.


[1,8,6,2,5,4,8,3,7]

```md

def maxArea(height):

    left = 0
    right = 1
    max_area = -float('inf')

    while right < len(height):
        dif = right - left

        area = min(height[left], height[right]) * dif
        max_area = max(area, max_area)

        print(f'{right} dif: {dif}')
        print(f'{right} area: {area}')
        print(f'{right} max_area: {max_area}')

        if height[left] < height[right]:
            left = right
            right += 1
        else: 
            right += 1

    return max_area

print(maxArea(height))

print(maxArea(height))

'''
1 dif: 1
1 area: 1
1 max_area: 1
2 dif: 1
2 area: 6
2 max_area: 6
3 dif: 2
3 area: 4
3 max_area: 6
4 dif: 3
4 area: 15
4 max_area: 15
5 dif: 4
5 area: 16
5 max_area: 16
6 dif: 5
6 area: 40
6 max_area: 40
7 dif: 6
7 area: 18
7 max_area: 40
8 dif: 7
8 area: 49
8 max_area: 49
49
'''

```
