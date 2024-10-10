def bubble_sort(arr):
    n = len(arr)
    iterations = []

    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False

        # Create a copy of the current state
        current_state = arr.copy()
        iterations.append(f'Iteration {i + 1}: {current_state}')

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap them if they are in wrong order
            if arr[j] > arr[j + 1]:
                # swap them if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Record the swap
                iterations.append(f'Swap: {arr[j]} and {arr[j + 1]} -> {arr}')
            
            # If no swapping ocurred, array is already sorted

    return arr, iterations

# Example usage
if __name__ == '__main__':
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", numbers)
    sorted_array, steps = bubble_sort(numbers.copy())
    print('\nSorting steps:')
    for step in steps:
        print(step)
    print('\nFinal sorted: array:', sorted_array)

'''
Sorting steps:
Iteration 1: [64, 34, 25, 12, 22, 11, 90]
Swap: 34 and 64 -> [34, 64, 25, 12, 22, 11, 90]
Swap: 25 and 64 -> [34, 25, 64, 12, 22, 11, 90]
Swap: 12 and 64 -> [34, 25, 12, 64, 22, 11, 90]
Swap: 22 and 64 -> [34, 25, 12, 22, 64, 11, 90]
Swap: 11 and 64 -> [34, 25, 12, 22, 11, 64, 90]
Iteration 2: [34, 25, 12, 22, 11, 64, 90]
Swap: 25 and 34 -> [25, 34, 12, 22, 11, 64, 90]
Swap: 12 and 34 -> [25, 12, 34, 22, 11, 64, 90]
Swap: 22 and 34 -> [25, 12, 22, 34, 11, 64, 90]
Swap: 11 and 34 -> [25, 12, 22, 11, 34, 64, 90]
Iteration 3: [25, 12, 22, 11, 34, 64, 90]
Swap: 12 and 25 -> [12, 25, 22, 11, 34, 64, 90]
Swap: 22 and 25 -> [12, 22, 25, 11, 34, 64, 90]
Swap: 11 and 25 -> [12, 22, 11, 25, 34, 64, 90]
Iteration 4: [12, 22, 11, 25, 34, 64, 90]
Swap: 11 and 22 -> [12, 11, 22, 25, 34, 64, 90]
Iteration 5: [12, 11, 22, 25, 34, 64, 90]
Swap: 11 and 12 -> [11, 12, 22, 25, 34, 64, 90]
Iteration 6: [11, 12, 22, 25, 34, 64, 90]
Iteration 7: [11, 12, 22, 25, 34, 64, 90]

Final sorted: array: [11, 12, 22, 25, 34, 64, 90]
'''