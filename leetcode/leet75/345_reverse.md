# 345. Reverse Vowels of a String

Given a string **s**, reverse only all the vowels in the string and return it.

The vowels are **'a'**, **'e'**, **'i'**, **'o'**, and **'u'**, and they can appear in both lower and upper cases, more than once.

## Example 1:

**Input:** s = "IceCreAm"
**Output:** "AceCreIm"

**Explanation:** The vowels in *s* are *['I', 'e', 'e', 'A']*. On reversing the vowels, s becomes *"AceCreIm"*.

## Example 2:

**Input:** s = "leetcode"
**Output:** "leotcede"

## Constraints:

* *1 <= s.length <= 3 * 105*
* *s consist of printable ASCII characters.*

## Intuition

Maybe I must run through all of the characters in the string to know if they are vowels or not.
Maybe I must store both: position and value of each found vowel.

Maybe I must run through all of the characters in the string to know if they are either vowels or not.
Maybe I must store both: position and value of each found vowel.

After doing that, the values must be reversed, and then put into the original index.

Maybe there can be two arrays to store the values, one with the value of the vowel, and the other one with the position of the vowel, this gives a memory complexity of O(2n), because it stores two arrays of values.

As it would run all over the array, it may have a time complexity of n, because it must run over every single value.

Are there any basic cases? i think no, as the sortest array size must be 1, and remember: the original value is a string, not an array.


## Algorithm

position=[]
value=[]
list_s=list(s)

for i, letter in enumarete(s):
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        position.append(int(i))
        value.append(letter)

for i in position:
    x = 0
    list_s[i] = value[x]
    x += 1

res = ''.join(list_s)

This code has 3 arrays and a string, which may make the memory complexity into O(3n + 1), which would be equals to O(n).

And the time complexity relays into separate loops, which would make it O(2n), which in summary would be O(n)

## Implementation

### Performance
Runtime: 27ms, Beats 56.98%
Memory: 15.00 MB, Beats 34.62%

### Code

Consider please that the comments in the code reduce its performance in time and memory, if you want to test it, I suggest you to delete them before running it in leetcode.

```py

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    # array for the position of each vowel
    position=[]
    # array for the value of each vowel
    value=[]
    # transform the string into an array so we can manipulate the values easily
    list_s=list(s)
    # index to run on each value of the reversed list
    x = 0

    for i, letter in enumerate(s):
        # If the code finds a vowel
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # store the position of the found vowel in the array 'position'
            position.append(int(i))
            # store the value of the found vowel in the array 'position'
            value.append(letter)

    # reverse the order of the array of vowels
    rev_value = value[::-1]

    for i in position:
        # print(f'this is the index {i}, this is the value {rev_value[x]}') <- to test the code in a local environment
        # store in the list_s, at the position given by i in position, the value of rev_value starting in 0
        list_s[i] = rev_value[x]
        # index to go to the next position in rev_value[x], in the next iteration
        x += 1

    # transform the array to a string
    res = ''.join(list_s)

    # return(print(res)) <- to test the code in a local environment
    return res

'''
# For test in local environment
if __name__ == '__main__':
    s = "IceCreAm"
    reverseVowels(s)
    s = "leetcode"
    reverseVowels(s)
'''

'''
# Test Results:
this is the index 0, this is the value A
this is the index 2, this is the value e
this is the index 5, this is the value e
this is the index 6, this is the value I
AceCreIm
this is the index 1, this is the value e
this is the index 2, this is the value o
this is the index 5, this is the value e
this is the index 7, this is the value e
leotcede
'''

