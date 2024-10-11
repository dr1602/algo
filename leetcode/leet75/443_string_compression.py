# 443. String Compression

''''
Given an array of characters chars, compress it using the following algo:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
a. If the group's length is 1, append the character to s.
b. Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the ne length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol. 

'''

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

# The answer of cortana

def compress(chars):
    if not chars:
        return 0
    
    # Initialize pointers
    left = 0
    arr = []

    while left < len(chars):
        right = left

        # Move right pointer to the end of the current sequence of the same character
        while right < len(chars) and chars[right] == chars[left]:
            right += 1

        # append the current character
        arr.append(chars[left])

        # If there is more than one occurrence of the character, append the count
        count = right - left
        if count > 1:
            for digit in str(count): #Convert count to string and append eca digit
                arr.append(digit)
            
        # Move the left pointer to the next new character
        left = right

    # Modify the original chars list in place to match the compressed version
    chars[:] = arr

    return len(arr)

# Propuesta de Solucion Personal

'''
Similarly with  the sliding window, I get 2 pointers, left and right
which iterate dinamicaly through to validate the repeated characters.

1. set the l value to 0
.... I cannot set a r with value of 1, because the array can have a length of
1

2. set the right value to 0
3. I create a input_char_arr
4. if the length is equals two 1, the value arr can be given to input_char_arr
    and input_char_var can be returned
5. at any other case we can run through the array, first compare the first two values
6. if the arr[left] != arr[rigth]
7. we input each value in the new array, at their current position.
8. if they are the same value, we can move right 1 position and we can repeat the process

def compress(chars):
    left=0
    right=1
    arr=[]

    for s in chars:
        if len(chars) == 0:
            return arr.append(s)
        
        if chars[left] != chars[right] and left - right == 1:
            arr.append(left)
            left += 1
            right += 1
        elif chars[left] != chars[right] and left - right != 1:
            arr.append(left)
            if (left - right) % 10 != 0:    
                arr.append((left - right)/10)
                arr.append((left - right)%10)
            else:
                arr.append(left - right
            left += 1
            right += 1

        elif chars[left] == chars[right]:
            right += 1
    
    return arr   

'''


'''
left = 0
right = 1

left, right += 1

print(left, right)  # Output: (1, 2)
'''