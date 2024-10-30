# 605. Can Place Flowers


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


'''
flowerbed = [1,0,0,0,1]
print(len(flowerbed))
'''