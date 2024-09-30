def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (low + high) // 2
        print(f'est es mid: {mid}')
        if arr[mid] < x:
            low = mid + 1
            print(f'est es low cuando mid menor a x: {low}')
        elif arr[mid] > x:
            high = mid - 1
            print(f'est es high cuando mid mayor a x: {high}')
        else:
            return mid
    
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 2
    result = binary_search(arr, x)
    if result != -1:
        print(f'Element is present at index: {str(result)}')
    else:
        print("Element is not present in array")
        
'''
est es mid: 2
est es high cuando mid mayor a x: 1
est es mid: 0
Element is present at index: 0
'''