'''
Longest Substring Without Repeating Characters

Given a string 's', find the length of the longest substring without repeating characters.

Example 1:
    Input: s = 'abcabcbb'
    Output: 3
    Explanation: The answer is 'abc', with the length of 3.

Example 2:
    Input: s = 'bbbbb'
    Output: 1
    Explanation: The answer is 'abc', with the length of 1.
    
Example 3:
    Input: s = 'pwwkew'
    Output: 3
    Explanation: The answer is 'wke', with the length of 3.
    Notice that the answer must be a substring, 'pwke' is a subsqequence and not a substring
    
Constrains:
    a. 0 <= s.length <= 5*10^4
    b. s consists of English letters, digits, symbols and spaces.    

'''

# Trabajando la solucion

'''

a. Tomo un elemento en el string y comparo si ya se habia visto antes
b. Si ya se habia visto antes, lo descarto
c. Si no lo he visto antes, lo sumo 1
d. con esta logica repaso todo el string una vez (porque son caracteres, no numeros)
e. y regreso aquellos valores cuya suma sea 1

IMPORTANTE, la cantidad maxima de caracteres es de la suma de letters, digits, symbols y spaces unicos en el idioma ingles. 

'''

# Mi solucion:

class Solution:
    def lengthOfLongestSubstrin(self, s: str) -> int:
        res = set(list(s))
        # res = int(len(set(list(s))))
        return res
    
if __name__ == '__main__':
    test_1 = Solution.lengthOfLongestSubstrin('s','abcabcbb')
    test_2 = Solution.lengthOfLongestSubstrin('s','bbbbb')
    test_3 = Solution.lengthOfLongestSubstrin('s','pwwkew')
    
    print(test_1)
    print(test_2)
    print(test_3)
    
# Solucion Asistida

class Solution:
    def lengthOfLongestSubstrin(self, s: str) -> int:
        # Dictionary to store last position of each character
        char_pos = {}
        
        # Start of current window
        start = 0
        
        # Maximum length found so far
        max_length = 0
        
        # Iterate through the string
        for current_pos, char in enumerate(s):
            # If we've seen this character before and it's in our current window
            if char in char_pos and char_pos[char] >= start:
                # Move the start of our window to just after the last ocurrence
                start = char_pos[char] + 1
            else:
                # UPdate max_length if current window is longer
                max_length = max(max_length, current_pos - start + 1)
                
            # Update last position of current character
            char_pos[char] = current_pos
            
        return max_length
    
# Test cases

def test_solution():
    solution = Solution()
    
    # Test case 1
    assert solution.lengthOfLongestSubstrin('abcabcbb') == 3
    
    # Test case 2
    assert solution.lengthOfLongestSubstrin('bbbbb') == 1
    
    # Test case 3
    assert solution.lengthOfLongestSubstrin('pwwkew') == 3
    
    # Additional test cases
    assert solution.lengthOfLongestSubstrin('') == 0
    assert solution.lengthOfLongestSubstrin(' ') == 1
    assert solution.lengthOfLongestSubstrin('au') == 2
    assert solution.lengthOfLongestSubstrin('aab') == 2
    print("All test cases passed!")
    
# Run test
if __name__ == "__main__":
    test_solution()
    
    
'''
Explicacion:

We can use the 'sliding window' technique with a dictionary/ hash map to keep track of characters and ther positions

'''

## Sliding window technique in Python:

'''
The sliding window techinque is a useful approach for solving problems that involve iterating over a sequence
of elements while maintaining a window of a fixed size. It's often used to optimize algorithms that would otherwise
have quadratic complexity.

## Why sliding window for quadratic time complexity?

Many algorithms that involve iterating over a sequence of elements can have quadratic time complexity, meaning their
time grows proportionally to the square of the input size. This can be inefficient for large input sizes.

    The sliding window technique can help optimize these algorithms by reducing the umber of redundant calculations.
Instead of re-evaluating the entire sequence for each possible window, it maitains a window of a fixed size and upstades
the calculations as the window slides along the sequence. This can significantly improve the time complexity to linear near-linear.

What is a 'Window'?

In the contestxt of the sliding window technique, a 'window' refers to a contiguous subarray or subsequence of elements
within the original sequence. The size of the window can be fixed or variable, depending on the specific problem.

## Key Points:

a. Fixed Size: in many cases, the window size is fixed. For example, in the maximum sum subarray problem, the window size is always 1.
b. Sliding: The window 'slides' along the sequence, one element at a time.
c. Updates: as the window slides, the calculations within the window are updated efficiently, avoid redundant computations.

Example 1:

Problem - Given an array of intergers, find the contiguous subarray with the largest sum

Solution:

'''

def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    
    print(range(len(nums)))
    
    for end in range(len(nums)):
        print(f'current_sum {current_sum}')
        current_sum += nums[end]
        print(f'nums[end] {nums[end]}')
        print(f'current_sum = nums[end] {current_sum}')
        
        print(f'max_sum {max_sum}')
        max_sum = max(max_sum, current_sum)
        print(f'max_sum {current_sum}')
        print(f'max_sum = max(max_sum, current_sum) {max_sum}')
        
        print(f'current_sum {current_sum}')
        if current_sum < 0:
            current_sum = 0
            start = end + 1
            
        return max_sum
        
max_subarray_sum([1, 2, 3, 3, 2, 1])

'''
Explanation:
a. We maintain a current_sum variable to keep track of the sum of the current window
b. If the current_sum becomes negative, we reset it to 0 and update the start index to the next element.
c. We keep track of the maximum sum encountered so far.
'''

'''
# Example 2: Longest Substring Without Repeating Characters

Problem: Given a string, find the length of the longest substring without repeating characters.

'''

def length_of_longest_substring(s):
    char_index = {}
    start = 0
    max_length = 0
    
    for end in range(len(s)):
        print(f'range(len(s)): {range(len(s))}')
        if s[end] in char_index and char_index[s[end]] >= start:
            print(f's[end]: {s[end]}')
            print(f'char_index: {char_index}')
            print(f'char_index[s[end]]: {char_index[s[end]]}')
            
            start = char_index[s[end]] + 1
            print(f'start: {start}')
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
        
    return max_length

print(length_of_longest_substring(['s','a','b','s','t','r','a','c','a']))

'''
range(len(s)): range(0, 9)
range(len(s)): range(0, 9)
range(len(s)): range(0, 9)
s[end]: s
char_index: {'s': 0, 'a': 1, 'b': 2}
char_index[s[end]]: 0
start: 1
range(len(s)): range(0, 9)
range(len(s)): range(0, 9)
range(len(s)): range(0, 9)
s[end]: a
char_index: {'s': 3, 'a': 1, 'b': 2, 't': 4, 'r': 5}
char_index[s[end]]: 1
start: 2
range(len(s)): range(0, 9)
range(len(s)): range(0, 9)
s[end]: a
char_index: {'s': 3, 'a': 6, 'b': 2, 't': 4, 'r': 5, 'c': 7}
char_index[s[end]]: 6
start: 7
6

Explanation:
a. We use a dictionary to keep track of the required characters and their counts.
b. If a character is found in the current window, we update the start index to the
next position after the last occurrence of the character.
c. We update the max_length if the current window is longer

'''

'''
Example 3: Minimum Window Substring

Problem: Given two string s and t, find the minimum window s such that it contains al the
characters from t.
'''

def min_window_substring(s, t):
    char_count = {}
    for char in t:
        # print(f'char: {char}')
        char_count[char] = char_count.get(char, 0) + 1
        # print(f'char_count[char]: {char_count[char]} ')
    
    required = len(char_count)
    formed = 0
    start = 0
    end = 0
    min_length = float('inf')
    window_size = float('inf')
    
    while end < len(s):
        char = s[end]
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                formed += 1
                
        while start <= end and formed == required:
            char = s[start]
            if char in char_count:
                if char_count[char] == 0:
                    formed -= 1
                char_count[char] += 1
            if end - start + 1 < window_size:
                window_size = end - start + 1
                min_window = s[start:end+1]
                
            start += 1
            
        end += 1
        
    return min_window if window_size != float('inf') else ''

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_substring(s, t)
    print(result)  # Output: "BANC"
    
