# 151. Reverse Words in a String

'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at
least on space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The
returned string should only have a single space separating the words. do not include any extra
spaces.

Example 1:
    Input: s = 'the sky is blue'
    Output: 'blue is  sky the'

Example 2:
    Input: s = 'a good    example'
    Output: 'example good a'
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string

Example 3:
    Input: '   hello    world  '
    Output: 'world hello'
    Explanation: Your reversed string should not contain leading trailing spaces.

Constraints:
a. 1 <= s.length <= 104
b. s contains English  letters (upper-case and lower-case), digits, and spaces ' '.
c. There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# EI Solution:

a. Split the string by spaces: This breaks the string into individual words, while ignoring any leading or trauling spaces.

b. Filter out empty strings: This step ensures that we remove extra spaces between words by filtering out empy strings from
the split.

c. Reverse the list of words: We then reverse the list of words to get them in the desired order.

d. Join the words with a single space: Finally, we join the reversed words using a single space between them
to form the final string.


'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Split the string by spaces, filter out empty strings (extra spaces), and reverse the words
        words = s.split() # This automatically removes extra spaces
        reversed_words = words[::-1] # Reverse the list of words
            
        return ' '.join(reversed_words) # Join the words with a single space

# Posible solution

'''

'   hello    world  '

1. validate if the space is empty, and continue the same validation until I find the first letter

'   h'

store position on h => 3

2. From that index, i my validate where is the next space, if any.

'hello '
store the position of o => 7

3. the process is repetead until the end of the string is reached.

Now, the trouble i have. How can you store this?
You can have pairs of counters that show the position in which the array start and ends,
stored in an array.
then you can use divde and conquer to swap the order both considering a original pair
as a unit.

[3,7]

and the process can be repeated so for

'    w', w => 12

and

'world ', d => 16

[3,7,12,16]

we divide and swap

[3,7][12,16]

we swap

[12,16][3,7]

if it is longer, the what we can do is to move the last pair to the first position, until
the last pair has been swapped.

.... the other problem would be, how to call the information???


'''

# Test

def reverseWords(s):
    words = s.split()
    print(f'words: {words}')
    reversed_words = words[::-1]
    print(f'reversed_words: {reversed_words}')
        
    return ' '.join(reversed_words) 

# Examples

if __name__ == '__main__':
    example_1 = 'the sky is blue'
    example_2 = 'a good    example'
    example_3 = '   hello    world  '
    
    print(reverseWords(example_1))
    print(reverseWords(example_2))
    print(reverseWords(example_3))

    '''
    words: ['the', 'sky', 'is', 'blue']
    reversed_words: ['blue', 'is', 'sky', 'the']
    blue is sky the
    words: ['a', 'good', 'example']
    reversed_words: ['example', 'good', 'a']
    example good a
    words: ['hello', 'world']
    reversed_words: ['world', 'hello']
    world hello
    '''


## Another possible solution:


def reverseWordsTwo(s: str) -> str:
    words = s.split()
    left, right = 0, len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        print(f'words: {words}')

    return ' '.join(words)
    
if __name__ == '__main__':
    example_1 = 'the sky is blue'
    example_2 = 'a good    example'
    example_3 = '   hello    world  '
    
    print(reverseWordsTwo(example_1))
    print(reverseWordsTwo(example_2))
    print(reverseWordsTwo(example_3))

    '''
    words: ['blue', 'sky', 'is', 'the']
    words: ['blue', 'is', 'sky', 'the']
    blue is sky the
    words: ['example', 'good', 'a']
    example good a
    words: ['world', 'hello']
    world hello
    '''
    

