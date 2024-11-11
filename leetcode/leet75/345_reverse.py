
'''
s = 'Icecream'

for letter in s:
    print(letter)
'''

# I
# c
# e
# c
# r
# e
# a
# m

'''
s = 'Icecream'
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in s:
    if letter in vowels:
        print(True)
    else:
        print(letter)
'''

# I
# c
# True
# c
# r
# True
# True
# m

'''
s = 'Icecream'
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in s:
    if letter.lower() in vowels:
        print(True)
    else:
        print(letter)
'''

# True
# c
# True
# c
# r
# True
# True
# m

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    position=[]
    value=[]
    list_s=list(s)
    x = 0

    for i, letter in enumerate(s):
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            position.append(int(i))
            value.append(letter)

    rev_value = value[::-1]

    for i in position:
        list_s[i] = rev_value[x]
        x += 1

    res = ''.join(list_s)

    return(res)

if __name__ == '__main__':
    s = "IceCreAm"
    reverseVowels(s)
    s = "leetcode"
    reverseVowels(s)

'''
AceCreIm
leotcede
'''