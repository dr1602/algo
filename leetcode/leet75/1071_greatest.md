# 1071. Greatest Common Divisor of Strings

For two strings **s** and **t**, we say "**t** divides **s**" if and only if **s = t + t + t + ... + t + t** (i.e., **t** is concatenated with itself one or more times).

Given two strings **str1** and **str2**, return the largest string **x** such that **x** divides both **str1** and **str2**.

## Example 1:
**Input:** str1 = "ABCABC", str2 = "ABC"
**Output:** "ABC"

## Example 2:
**Input:** str1 = "ABABAB", str2 = "ABAB"
**Output:** "AB"

## Example 3:
**Input:** str1 = "LEET", str2 = "CODE"
**Output:** ""

## Constraints:

* *1 <= str1.length, str2.length <= 1000*
* *str1* and *str2* consist of English uppercase letters.

## How to solve (ideas)

* I think it all depends on the shortest string, maybe the shortest string, helps defining the largest string that divides str1 and str2

1. you can take the first element of the shortest str1, and compare if ti appears at least once
... if it appears once, you take the first two and repeat the process..
... at this point if the first elements doesn't apear, then the strings area different, and the resutl is ''

... for what I have seen is that, the elements area in order from left to right..., so you don't have to check through out the entire longest string, you can do something like this:
a. str1 = "ABCABC"
b. str2 = "ABC"

a. I compare and check the length of each of them, and choose the shortest....

S[0] = A
L[0] = A

If the weren't similar, and as they in theory ordered, they would be different, then de result should be:
''

a. if shortest had only 1 element, then I would compare the string with the longest string, if the shortest would be the same as each element length(S), then the result would be S[0]

B. They both are similar, then I expand the window of comparission for both:
S[0:1] = AB
L[0:1] = AB

a. if they are different, then the return would be: ''
b. if shortest had only 1 element, then I would compare the string with the longest string, if the shortest would be the same as each element length(S), then the result would be S[0]
c. They both are similar, then I expand the window of comparission for both:

And the process is reapetead...

the complexity, yes the speed could O(n) because it has to iterate at each element to get the final result, both, as we work with the windows, in the wors scenario we would have a comparission of n.

## Test

```
def gcdOfStrings(str1, str2):
    
    result = ''
    x = 0

    for i in (range(len(str1), len(str2))):
        if i == 0 and str1[i:i+1] != str2[i:i+1]:
            result = ''
            return result
        elif str1[i:i+1] != str2[i:i+1]:
            break
        else:
            if len(str1) > len(str2):
                result += str1(i)
            else:
                result += str2(i)

    while x < max(len(str1),len(str2)):
        if len(str1) > len(str2):
            if result != str1[x:len(result)]:
                result = ''
                return result
            else:
                x += len(result)
        else:
            if result != str2[x:len(result)]:
                result = ''
                return result
            else:
                x += len(result)

    return result
```

## Ayudas propias para entender el algoritmo

```py
str1 = "ABCABC"

print(str1[0:1])
print(len(str1))

print(str1[0:len(str1)])
print(str1[2:len(str1)])
```

#### Didn't work, lol

## suggested answer

```
def greatestCommonDivisorOfStrings(str1, str2):
    # Find the smaller string
    smaller_string = min(str1, str2, key=len)

    # Iterate over substrings from longest to shortest
    for i in range(len(smaller_String), 0, -1):
        substring = smaller_string[:i]
        if str1.count(substring) * substring == str1 and str2.count(substring) * substring == str2:
            return substring

    return ''

```

### Efficiency
13 ms Beats 72.40%
11.84 MB Beats 6.77%

### Explanation for smaller_string = min(str1, str2, key=len)

The **smaller_string = min(str1, str2, key=len)** line in the code finds the smaller string between **str1** and **str2** based on their lengths.

Here's a breakdown of what each part does:

* **min(str1, str2):** This part compares **str1** and **str2** and returns the smaller string based on their lexicographical order (alphabetical order).

* **key=len:** This argument specifies that the comparison should be based on the length of the strings instead of their lexicographical order. This means that the function will return the string with the shorter length.

In essence, this line efficiently determines which of the two strings is shorter without explicitly calculating their lengths. It's a concise and efficient way to find the smaller string for further processing in the algorithm.

### Explanation for range(len(smaller_string), 0, -1)

The range(len(smaller_string), 0, -1) expression in Python creates a range of numbers that starts from len(smaller_string) - 1 (the last index of the smaller string) and goes down to 0, decrementing by 1 in each step.

Here's a breakdown of what each part does:

* **len(smaller_string):** This calculates the length of the **smaller_string** string.

* **0:** This is the end value of the range. The range will stop when the current value reaches 0.

* **-1:** This is the step value, indicating that the range should count down from **len(smaller_string) - 1** to 0.

This range is used in the for loop to iterate over the substrings of smaller_string in reverse order, starting from the longest substring and going down to the shortest. This is because the largest common divisor is most likely to be a longer substring.

### Explanation for if str1.count(substring) * substring == str1 and str2.count(substring) * substring == str2:

The line **if str1.count(substring) * substring == str1 and str2.count(substring) * substring == str2:** checks if the given **substring** can be repeated to form the entire **str1** and **str2** strings.

Here's a breakdown of what each part does:

* **str1.count(substring):** This counts the number of times the **substring** appears in the str1 string.

* **substring:** This is the substring being checked.

* **str1.count(substring) * substring:** This multiplies the count of the substring in **str1** with the substring itself. If the substring can be repeated to form **str1**, this expression will be equal to **str1**.

* **str2.count(substring) * substring**: This does the same for the **str2** string.

* **if str1.count(substring) * substring == str1 and str2.count(substring) * substring == str2:**: This checks if both conditions are true. If both conditions are true, it means the **substring** can be repeated to form both **str1** and **str2**, and therefore it is the largest common divisor.

If both conditions are true, the function returns the **substring**. Otherwise, it continues checking other substrings until a match is found or all substrings have been checked.

## Best in speed (in theory)

```py

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''

    def gdc(a, b):
        while b:
            a, b = b, a % b
        return a

    gdc_length = gdc(len(str1), len(str2))

    return str1[:gdc_length]

```

### Efficiency
0 ms Beats 100s%
11.74 MB Beats 25.75%

## Explanation

The gdc function you've provided is a classic implementation of the Euclidean algorithm to calculate the greatest common divisor (GCD) of two numbers.

Here's a breakdown of what it does:

* **Base Case:** The function takes two numbers a and b as input. If b is 0, it means a is the GCD, so the function returns a.

* **Recursive Call:** If b is not 0, the function recursively calls itself with b as the new a and the remainder of a divided by b as the new b. This process continues until b becomes 0.

* **Return GCD:** When b becomes 0, the current value of a is the GCD, so the function returns it.

In the context of the gcdOfStrings function:

* The gdc function is used to calculate the GCD of the lengths of the two strings str1 and str2.
* The GCD of the lengths represents the maximum possible length of a common substring that can be repeated to form both strings.
* The gdc_length variable stores the calculated GCD.
* Finally, the function returns a substring of str1 with a length equal to gdc_length, which is the largest common divisor of the two strings.

In summary:

The gdc function is a core component of the gcdOfStrings function, efficiently calculating the GCD of the string lengths to determine the maximum possible length of the common substring.
