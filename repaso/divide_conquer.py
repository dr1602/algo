# Divide-and-Conquer (Dividir y Vencer), QuickSort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # funcion recursiva
        return quicksort(left) + middle + quicksort(right)
    
# Example
if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quicksort(arr))
    # [1, 1, 2, 3, 6, 8, 10]