# 605. Can Place Flowers


# def canPlaceFlowers(flowerbed, n):
#     """
#     :type flowerbed: List[int]
#     :type n: int
#     :rtype: bool
#     """
#     if (len(flowerbed) - 2) >= (2*n + 1):
#         return True
#     else:
#         return False



flowerbed = [1,0,0,0,1]
print(len(flowerbed))
# 5

for flower in flowerbed:
    print(flower)

# 1
# 0
# 0
# 0
# 1

for i, flower in enumerate(flowerbed):
    print(f'This is i: {i}' )
    print(f'This is flower: {flower}' )

# This is i: 0
# This is flower: 1
# This is i: 1
# This is flower: 0
# This is i: 2
# This is flower: 0
# This is i: 3
# This is flower: 0
# This is i: 4
# This is flower: 1

print(range(1, len(flowerbed) - 1))
# range(1, 4)

for i in range(1, len(flowerbed) - 1):
    print(f'This is i: {i}' )

# This is i: 1
# This is i: 2
# This is i: 3