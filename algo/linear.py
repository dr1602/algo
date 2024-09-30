def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == '__main__':
    from linear import linear_search
    
    arr = [2, 3, 4,10 ,40]
    x = 10
    result = linear_search(arr, x)

    if result != -1:
        print(f'Element is present at index: {str(result)}')
    else: 
        print(f'Element is not present in the array')
        
    # Element is present at index: 3