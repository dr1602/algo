# 7. Reverse Integer

'''
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to o outside the signed 32-bit integer range
[-231, 231 - 1], the return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned)

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = /120
    Output: -21

Constrains:
    -231 <= x <= 231 - 1
'''

def reverse(x):
    '''
    :type x: int
    Lrtype: int
    '''

    # Handle the sign separately
    is_negative = x < 0

    # Convert to positive number for easier handling
    x = abs(x)

    # Initialize reversed number
    reversed_num = 0

    # Reverse the number digit by digit
    while x > 0 :
        # Get the last digit
        digit = x % 10
        # Remove the last digit from %
        x //= 10

        # Check for potential overflow before adding new digit

        if reversed_num > ( 2 ** 31 - 1 )// 10:
            return 0
        

        # Build the reversed number
        reversed_num = (reversed_num * 10) + digit

    # Apply the sign and check for negative overflow
    if is_negative:
        reversed_num = -reversed_num

        # here it is iterating over the limits of the problem
        if reversed_num < -2**31:
            return 0
        
    # Check for positive overflow
    elif reversed_num > 2 ** 31 - 1:
        return 0
    
    return reversed_num
    
if __name__ == '__main__':

    # Test cases
    test_cases = [
        123,            # Should return 321
        -123,           # Should return -321
        120,            # Should return 21
        0,              # Should return 0
        1534236469,     # Should return 0
    ]

    # Run test cases
    for test in test_cases:
        result = reverse(test)
        print(f'Input: {test}')
        print(f'Output: {result}')
        print('-' * 20)


'''
Explanation and complexity analysis:

Approach Used:
1. Mathematical Approach with digit-by-digit reversal:
    a. Extract digits using modulo (%) and integer division (//)
    b. Build reversed number while checking for overflow
    c. Handle negative numbers separately.

Key steps:
    1. Handle the sign separately to simplify the logic
    2. Extract digits one by one from right to left usinf modulo
    3. Build the reversed number by multiplying by 10 and adding new digits
    4. Check for potential overflow at each step
    5. Restore the sign at the end

Time Complexity:
    a. Worst Cases: O(logn), where n is the input number
    b. This is because we process each digit once, and the number of digits in a number is log10(n)

Space Coplexity:
    a. O(1) - constant space
    b. We only use a few variables regardless of input size:
        - reversed_num
        - is_negative
        - temporary variables for calculations

Key Points about the Solution
    a. Overflow Handling:
        - Checks for overflow before adding each new digit
        - Handles both positive (2^31 - 1) and negative (-2^31) bounds
        - return O if overflow would occur

    b. Sign Handling:
        - Separates sign handling from digit reversal
        - Reapplies sign at the end
        - Simplifies the main logic
    
    c. Edge Cases Handled
        - Negative numbers
        - Numbers ending in zero
        - Numbers that would cause overflow
        - Zero input

    4. No String Conversion
        - Solves the problem mathematically without converting to string
        - This is more efficient and meets the spirit of the problem.


'''