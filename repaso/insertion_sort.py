# Sorting (Ordenamiento) con Búsqueda Binaria
# Ordenamietno por Inserción (Insertion Sort) con Búsqueda Binaria para optimizar la inserción

def binary_inserion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # encuentra la posicion donde insertar el elemento usando busqueda binaria
        left, right = 0, i - 1
        # left = 0, right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        # Mueve los elementos para insertar el nuevo elemento
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key
    return arr

# Example
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(binary_inserion_sort(arr))
    # [11, 12, 22, 25, 34, 64, 90]