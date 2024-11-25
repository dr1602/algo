s = "ab"

t = "baab"

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    index = 0

    for i in t:
        if index == len(s):
            print(f'index: {index}')
            print(f'len(s): {len(s)}')
            return True
        elif i == s[index]:
            print(f'i: {i}')
            print(f's[index]: {s[index]}')
            print(f'index: {index}')
            index += 1
    
    return len(s) == index


result = isSubsequence(s, t)
print(result)

'''
#s Test

t = "ahbgdc"

print(t[2])

# b

s = "Python programming"

position_0 = s.index("prog")
position_1 = s.index("P")
position_2 = s.index("p")
# position_3 = s.index("G")

# Traceback (most recent call last):
#   File "/root/algo/leetcode/leet75/392_sub.py", line 16, in <module>
#     position_3 = s.index("G")
#                  ^^^^^^^^^^^^
# ValueError: substring not found

position_4 = s.index("g")

print(position_0, position_1, position_2, position_4)

# 7 0 7 10

'''