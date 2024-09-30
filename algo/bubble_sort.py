# Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # print(f'this is i: {i}')
        for j in range (0, n - i - 1):
            # print(n - i - 1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f'this is arr[j]: {arr[j]}')
                print(f'this is arr[j + 1]: {arr[j + 1]}')
                
           
if __name__ == '__main__': 
    arr = [64, 34, 25, 12, 22, 11, 90 ]
    # print(len(arr))
    # 7
    bubble_sort(arr)
    print(f'Sorted array: {arr}')

# Sorted array: [11, 12, 22, 25, 34, 64, 90]