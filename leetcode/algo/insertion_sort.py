# Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]

        # Move elements of arr[0..i - 1], that are
        # greater than the key to one position ahead of their current position

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Example usage

if __name__ == '__main__':
    data = [64, 25, 12, 22, 11]
    insertion_sort(data)
    print('Sorted array:', data)

# Explanation:
'''
1. Iteratoin through the array: The outer loop iterates from the second element (index 1) 
to the laste element (index n-1)
2. Insert the current element: The inner loop compares the current element (key) with the elements
in the sorted part of the array. If the current element is smaller than the previous element, it shifts
the previous element to the right.
3. Place the current element: Once the correct position is found, the current element is inserted into
its place.
'''

# Whe insertion sort is a good choice.

'''
a. Small datasets: Insertion sort is generally more efficient than algorithms like quicksort or mergesort
for small datasets.
b. Partially sorted data: If the data is already partially sorted, insertion sort can be very efficient.
c. Online algorithms: Insertion sort can be used as an online algorithm for small datasets, it's not
the best choice for larga datasets due to its quadratic time complexity. For larger datasets, algoritms
like quicksort or mergesort are typicallu preferred.

'''