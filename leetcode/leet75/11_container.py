# Two Pointers
# 11. Container with most water

height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):

    left = 0
    right = len(height) - 1
    max_area = -float('inf')

    while left < right:

        area = min(height[left], height[right]) * (right - left)
        max_area = max(area, max_area)

        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1

    return max_area

print(maxArea(height))


'''
Classic: Container with most water problem.

In this problem, you want to find the two lines in the height list that can form
the container holding the most water.

The container's area is determined by the shorter of the two heights and the horizontal
distance between them.

a. Pointers movement: you need to decide whether to move left or right based on their 
relative heights. Always move the pointer pointing to the shorter wall, as moving
the taller wall cannot increase the area.
'''
