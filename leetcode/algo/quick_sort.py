# Quick sort

def quicksort(arr):
    ''' Sorts an array using quicksort algorithm.'''

    if len(arr) <= 1:
        return arr
    
    # tomar el valor que esta justo en la posicion media de la longitud del array en este caso 2
    pivot = arr[len(arr) // 2]
    print(f'pivot: {pivot}')

    # guardamos en un array llamado left, todos los valores dentro del array menores al valor en el indice de en medio
    left = [x for x in arr if x < pivot]
    print(f'left: {left}')

    # guardamos en medio, todos los valores iguales a pivot
    middle = [x for x in arr if x == pivot]
    print(f'middle: {middle}')

    # guardamos en un array llamado right, todos los valores dentro del array mayores al valor en el indice de en medio
    right = [x for x in arr if x > pivot]
    print(f'right: {right}')

    # repetimos el porcesos en este return para asegurarnos de que los subarrays seran acomodados.
    return quicksort(left) + middle + quicksort(right)

# Example usage
if __name__ == '__main__':
    data = [64, 25, 12, 22, 11]
    sorted_data = quicksort(data)
    print('Sorted array:', sorted_data)


'''
pivot: 12
left: [11]
middle: [12]
right: [64, 25, 22]
pivot: 25
left: [22]
middle: [25]
right: [64]
Sorted array: [11, 12, 22, 25, 64]
'''