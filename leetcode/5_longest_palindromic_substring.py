# 5. Longest Palindromic Substring

'''
Given a strin s, return the longest palindromic substring in s.

Example 1:
    Input: s = 'babad'
    Output: 'bab'
    Explanation: 'aba' is also a valid answer.
    
Example 2:
    Input: s = 'cbbd'
    Output: 'bb'
    
Constrains:
    a. 1 <= s.length <= 1000
    b. s consist of only digits and English

'''

### Trabajando la solucion ###

'''
Steps:

~ I take the first and the last element and compare them
~ I check the first two positions, if they are equal.
    . if they are, store as a palindrome
~ then i check the third and so on to reach n.
    . if you find a longer one, substitute the original

to not miss a single palindrome
~ start in position 2, check if to 2 and 3 are equal
~ I check 2, 3, and 4 positions, if they are equal.
    . if they are, store as a palindrome
~ then i check the third and so on to reach n.
    . if you find a longer one, substitute the original
    
this give a O(n^2) but those not solve if it is a palindrome, it only shows
if the nearby elements are exactly equal

if s % 2 = 0, it means that the first half of the array most be equal to the second half.
    when switched.
    
on the other hand, if s % 2 != 0, it means that in the upper rounded half, the element must be
different to the others, but still, the first half and the second half are the same.

I think the solution may be a divide and conquer approach.


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        # Initialize variable to keep track of the longest palindrome
        longest_start = 0
        longest_length = 1
        
        # Function to expand around center
        def expand_around_center(left: int, right: int) -> None:
            nonlocal longest_start, longest_length
            
            # Expand while within bounds an d characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > longest_length:
                    longest_start = left
                    longest_length = current_length
                left -= 1
                right += 1
                
        # Check again each position as a potential center
        for i in range(len(s)):
            # Odd length palindromes
            expand_around_center(i, i)
            # Even length palindromes
            if i < len(s) - 1:
                expand_around_center(i, i + 1)
                    
        return s[longest_start:longest_start + longest_length]
        
if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('a'))
    print(Solution().longestPalindrome('ac'))
    print(Solution().longestPalindrome('racecar'))
    print(Solution().longestPalindrome('aabbaa'))
    
        
# Test cases
def test_longest_palindrome():
    solution = Solution()
    
    # Test case 1
    assert solution.longestPalindrome('babad') in ['bab', 'aba'], 'Test case failed'
    
    # Test case 2
    assert solution.longestPalindrome('cbbd') == 'bb', 'Test case 2 failed'
    
    # Additional test cases
    assert solution.longestPalindrome('a') == 'a', 'Single charactert test failed'
    assert solution.longestPalindrome('ac') == 'a', 'Two different characters test failed'
    assert solution.longestPalindrome('racecar') == 'racecar', 'Odd length palindrome test failed'
    assert solution.longestPalindrome('aabbaa') == 'aabbaa', 'Even length palindrome test failed'
    
    print('All test casses passed!')
            
