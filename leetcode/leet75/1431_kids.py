# 1431. Kids With the Greatest Number of Candies

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    for i in candies:
        if max < i:
            max = i
    
    for index, value in enumerate(candies):

        if (max - value) > extraCandies:
            candies[index] = False
        else:
            candies[index] = True

    return candies


if __name__ == '__main__':
    ## Test Case 1
    candies = [2,3,5,1,3]
    extraCandies = 3

    result = kidsWithCandies(candies, extraCandies)
    print(result)

    ## Test Case 2
    candies_1 = [4,2,1,1,2]
    extraCandies_1 = 1

    result_1 = kidsWithCandies(candies_1, extraCandies_1)
    print(result_1)

    ## Test Case 3
    candies_2 = [12,1,12]
    extraCandies_2 = 10

    result_2 = kidsWithCandies(candies_2, extraCandies_2)
    print(result_2)


'''
candies = [2,3,5,1,3]
extraCandies = 3

# for i, j in candies:
#     print(i)
#     print(j)

maxCandies = max(candies)

for index, value in enumerate(candies):
    candies[index] = (maxCandies - value) <= extraCandies

print(candies)
'''

'''
for index, value in enumerate(candies, start=1):
    print(f"Index: {index}, Value: {value}")
'''
