# Selection sort

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i

        print(f'len[i]: {arr[i]}, i: {i}')

        for j in range(i+1, n):
            # if the first value is lower than the second in the current selection
            if arr[j] < arr[min_idx]:
                # walk from the first value to the second
                min_idx = j

                print(f'len[j]: {arr[j]}, j: {j}')
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f'arr[i]: {arr[i]}, arr[min_idx]: {arr[min_idx]}')

# Ejemplo de use:

if __name__ == '__main__':
    data = [ 64, 25, 12, 22, 11]
    selection_sort(data)
    print('Sorted array: ', data)

# Explicacion:

'''

1. Iteracion externa: recorre el arreglo desde el primer elemento hasta el penultimo.
2. Encontrar el minimo: En cada iteracion, se busca el elemento mas pequeno en la sublista no
ordenada
3. Intercambio: El elemento mas pequeno se intercambia ocn el primer elemento de la sublista no ordenada.

'''

# Mejor caso de uso
'''
NO es generalmente la mejor opcion para grandes conjuntos de datos. Sin embargo, podria ser util en situaciones como:
a. Ordernar pequenas lsitas de elementnos: por ejemplo, ordenar los elementos de una configuracion en un programa.
b. Implementar un algoritmo mas complejo: selection sort podria utilizarse como un subalgoritmo dentro de un algoritmo
mas complejo.
c. Enesenanza: es un algoritmo sencillo de entender y explicar, por lo que es ideal para introducir los conceptos basicos
de ordenamiento.
'''
