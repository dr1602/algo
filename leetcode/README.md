# Data structures:

1. Arrays
2. Linked lists
3. Stack
4. Queues
5. Sets
6. Maps
7. Binary Trees
8. Heaps
9. Graphs

# Algorithms:

1. Sorting
2. Searching
3. binary search
4. Divide-and-conquer
5. Dynamic programming and memorization
6. Greedy algorithms
7. Recursion
8. Graph traversal, breadth and depth-first

## Sorting

### Bubble Sort

**How it works**: Repeatedly steps through the list, compares adjacent elements and swaps them if they're in the wrong order.

**Time complexity**: O(n^2) 

**Space Complexity**: 0(1)

**Best for**: Small datasets, educational purposes.

**Space Complexity**: Stablew

[Example](/algorithms/bubble_sort.py)   

### Selection Sort

**How it works**: Finds the minimum element in the unsorted portion and places it at the beginning.

**Time complexity**: O(n^2) 

**Space Complexity**: 0(1)

**Best for**: Small datasets, minimizing memory writes.

**Space Complexity**: Unstable

[Example](/algorithms/selection_sort.py)

### Insertion Sort

**How it works**: Builds final array one item at a time, by constantly inserting a new element into a sorted portion.

**Time complexity**: O(n^2) 

**Space Complexity**: 0(1)

**Best for**: Small datasets, nearly sorted arrays.

**Space Complexity**: Stable

### Quick Sort:

**How it works**: Uses divided-and-conquer strategy, selects a 'pivot' and partitions array around it.

**Time complexity**: Average O(n log n), Worst O(n^2) 

**Space Complexity**: 0(log n)

**Best for**: Large datasets, general-purpose sorting

**Space Complexity**: Unstable

### Merge Sort:

**How it works**: Divides array into two havles, sorts them and then merges the sorted halves.

**Time complexity**: O(n log n) 

**Space Complexity**: 0(n)

**Best for**: Large datasets, stable sorting needed

**Space Complexity**: Stable

### Heap Sort:

**How it works**: Builds a heap data structure and repeatedly extracts the maximum element

**Time complexity**: O(n log n) 

**Space Complexity**: 0(1)

**Best for**: Large datasets, memory constraints

**Space Complexity**: Unstable

## Non-Comparison Based Sorts

### Counting Sort

**How it works**: Counts occurrences of each element and reconstructs the sorted array

**Time complexity**: O(n + k) where k is the range of input 

**Space Complexity**: 0(k)

**Best for**: Integers with known range

**Space Complexity**: Stable

### Radix Sort

**How it works**: Sorts numbers digit by digit, from least significant to most significant.

**Time complexity**: O(d * (n + k)) where d is the number of digits.

**Space Complexity**: 0(n + k)

**Best for**: Integers or strings with fixed-length

**Space Complexity**: Stable

### Radix Sort

**How it works**: Sorts numbers digit by digit, from least significant to most significant.

**Time complexity**: O(d * (n + k)) where d is the number of digits.

**Space Complexity**: 0(n + k)

**Best for**: Integers or strings with fixed-length

**Space Complexity**: Stable

### Bucket Sort

**How it works**: Distributes elements into buckets and sorts buckets individually.

**Time complexity**: Average O(n + k), Worst O(n^2)

**Space Complexity**: 0(n + k)

**Best for**: Uniformly distributed data over a range

**Space Complexity**: Stable

## Special Purpose Sorts

### Shell sort

**How it works**: Variation of insertion sort that allows swapping of far elements.

**Time complexity**: Depends on gap sequence, typically O(n log n) to O(n²)

**Space Complexity**: 0(1)

**Best for**: Medium-size datasets

**Space Complexity**: Unstable

### Tim sort

**How it works**: Hybrid of merge sort and insertion sort, used as Python's built-in sort

**Time complexity**: O(n log n)

**Space Complexity**: 0(n)

**Best for**: Real-world data, partially sorted arrays

**Space Complexity**: Stable

## Comparison of Use Cases

### Best for Small Arrays (n<50)

a. Insertion Sort
b. Bubble Sort
c. Selection Sort

### Best for Medium Arrays (50< n < 1000)

a. Shell Sort
b. Quick Sort
c. Merge Sort

### Best for Large Arrays (n > 1000)

a. Quick Sort
b. Merge Sort
c. Heap Sort

### Beast for Nearly Sorted Data

a. Insertion Sort
b. Tim Sort

### Best for Limited Memory

a. Heap sort
b. Selection Sort
c. Shell Sort

### Best for Stability Requirement

a. Merge Sort
b. Tim Sort
c. Insertion Sort

