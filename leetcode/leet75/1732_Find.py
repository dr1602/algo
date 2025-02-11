def kidsWithCandies(gain):
    highest_gain = 0
    prefix = [0] * len(gain)
    prefix[0] = gain[0]

    if prefix[0] > highest_gain:
        highest_gain = prefix[0]

    for i in range(1, len(gain)):
        prefix[i] = prefix[i-1] + gain[i]

        if prefix[i] > highest_gain:
            highest_gain = prefix[i]
    
    return highest_gain

if __name__ == '__main__':
    test_one = [-5,1,5,0,-7]
    test_two = [-4,-3,-2,-1,4,3,2]
    -4-7-9-10-6 -3 -1
    result_one = kidsWithCandies(test_one)
    result_two = kidsWithCandies(test_two)

    print(result_one)
    print(result_two)