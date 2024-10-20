
string1 = 'abcdefg'
string2 = 'hij'

'''
print(string1[0])
print(range(len(string1)-1))

for i in range(len(string1)-1):
    print(i)

# Test:
# 0
# 1
# 2
# 3
# 4
# 5

print(string1[1:3])

string1 += string2[1]

print(string1)
'''

def mergeAlternately(word1, word2):
    alt_string = 's'
    # in the worst case scenario, the entire array would be duplicated, giving a complexity in space of n

    for i in range(min(len(word1),len(word2))-1):
        alt_string += str(word1[i])
        alt_string += str(word2[i])

        # in this case, the worst case scenario of spead is to run the longest array, which would give a time complexity of n

    if len(word1) > len(word2):
        alt_string +=  str(word1[len(word2):len(word1)+1])
    elif len(word2) > len(word1):
        alt_string += str(word2[len(word1):len(word2)+1])
    else:
        return alt_string

    return alt_string

result = mergeAlternately(string1, string2)
print(result)