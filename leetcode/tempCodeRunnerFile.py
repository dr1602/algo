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