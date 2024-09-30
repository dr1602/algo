def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        merge(arr, left_half, right_half)
        
def merge(arr, lef_half, right_half):
    i = j = k = 0
    
    while i < len(lef_half) and j < len(right_half):
        if lef_half[i] <= right_half[j]:
            arr[k] = lef_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            
        k += 1
    
    while i < len(lef_half):
        arr[k] = lef_half[i]
        i += 1
        k += 1
        
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
        
if __name__ == '__name__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    print(f'Sorted array: {arr}')