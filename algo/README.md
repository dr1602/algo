# Algo

## Sorting

Sorgin algo arrange elements in a specific order, such as ascending or descending. Here are two common sorting algos.

### Bubble Sort

a. Explanation: Compares adjacent elements and swaps them if they are in the wrong order. Repeats this process until de list is sorted.
b. Time complexity: O(n^2) in the worst case, O(n) in the best case

[Example](bubble_sort.py)

### Merge Sort

a. Explanation: Divides the list into halves, sorts each half recusively, and then merges the sorted halves.
b. Time complexity: O(n log n) in al cases

[Example](merge_sort.py)

## Searching

Searching algorithms find the position of a specific element in a list.

### Linear Search

a. Explanation: Iterates through the list sequentially until the element is found or the end is reached
b. Time complexity: O(n) in the worst case

[Example](linear.py)

### Binary Search (for sorted lists)

a. Explanation: Divides the list in half repeatedly until the element is found or the search space is empy.
b. Time complexity: O(log n) in the worst case

[Example](binary_search.py)

# Divide and conquer

Divide and conquer algorithms break down a problem into smaller subproblems, solve the subproblems recursively, and then comibne the solutions to solve the original problem.

## Merge Sort

We already saw it. Here's a breakdown of this divide and conquer approach:
a. divide: divide the array into two halves
b. conquer: recursively sort each half.
c. combine: merge the sorted halves into a single sorted array.

## Dynamic Programming / Memoization

Dynamic programming is an optimization technique that avoids redundant calculations by sorting intermeidate results. Memoization is a specific implementation of dynamic programming where results are sorted in a chache.

[Example](fibonacci.py)

Explanation:

a. The moemo ditionary stores previously calculated Fibonacci numbers
b. If n is already in the memo, the result is returned directly.
c. Otherwise, the Fibonacci number is calculated recursively and sotred in the memo for future use.

## Greedy Algorithms

Greedy algorithms make locally optimal choices at each step, hopin to reach a globally optimal solution.

[Example](greedy.py)

Explanation:
a. Sorts the coins in descending order
b. Greedily selects the largest coin that is less than or equal to the remaining amount.
c. Repetas until the amount is zero
