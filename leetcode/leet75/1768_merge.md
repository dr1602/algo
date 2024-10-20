# 1768. Merge Strings Alternately

You are given two strings **word1** and **word2**. Merge the strings by adding letters in alternating order, starting with **word1**. If a string is longer than the other, append the additional letters onto the end of the merfed string.

Return *the merged string*.

## Example 1

**Input:** word1 = 'abc', words2 = 'pqr'
**Output:** 'apbqcr'
**Explanation:** The merged string will be merged as so:
    word1:   a b c
    word2:    p q r
    merged:  apbqcr

## Example 2

**Input:** word1 = 'ab', words2 = 'pqrs'
**Output:** 'apbqcr'
**Explanation:** The merged string will be merged as so:
    word1:   a b
    word2:    p qrs
    merged:  apbqrs

## Example 3

**Input:** word1 = 'abcd', words2 = 'pq'
**Output:** 'apbqcr'
**Explanation:** The merged string will be merged as so:
    word1:   a b cd
    word2:    p q
    merged:  apbqcd

## Constraints:

* 1 <= word1.length, word2.length <= 100
* word1 and word2 consist of lowercase English letters.

## First try

1. we first need to divide each string, so we can reaaranged it.
* It is important to consider that, the first string well be the first to be placed
* The number of rearangements will be limited to the length of the second array, as long as it is equals to lower than the first one
* This inside may be useful to save memory, as we will limit the number of operations...

1. we compare the length
2. at each string we spread the number of characters equals to the shortest length
3.  we place first the element of the first string...
4. the we place the eleemnt of the second string...
5. we repeat this two operations until we reach the number of operations equals too the length of the shortest array...
6. if there is a complement, we add the complementary string of any strings


### Better than 60%
```

def mergeAlternately(word1, word2):
    alt_string = ''
    # in the worst case scenario, the entire array would be duplicated, giving a complexity in space of n

    for i in range(min(len(word1),len(word2))):
        alt_string += str(word1[i])
        alt_string += str(word2[i])

        # in this case, the worst case scenario of spead is to run the longest array, which would give a time complexity of n

    if len(word1) > len(word2):
        alt_string +=  str(word1[len(word2):len(word1)+1])
    elif len(word2) > len(word1):
        alt_string += str(word2[len(word1):len(word2)+1])
    else:
        return alt_string

    return alt_string


```

## Most optimal solution (speed)
Actually not, after sending it, it was better only than 45.10% in speed with 16ms
11.64 MB to beat 48.26% in memory.

```py

def mergeAlternately(word1, word2):
    ret = ''
    curr = 0

    while curr<len(word1) and curr<len(word2):
        ret += word1[curr]
        ret += word2[curr]
        curr += 1

    if curr == len(word1):
        return ret + word2[curr:]
    else:
        return ret + word1[curr:]

```

## Most optimal solution (memory)

Well, after the test the result was:
10ms Beats 87.66%
11.92MB Beats 17.64%

```py
def mergeAlternately(word1, word2):
    merged = ''

    for i in range(min(len(word1),len(word2))):
        merged += word1[i]
        merged += word2[i]

    if len(merged) != (len(word1) + len(word2)):
        if len(word2) > len(word1):
            merged += word2[i+1:len(word2)]
        else:
            merged += word1[i+1:len(word1)]

    return merged
```
