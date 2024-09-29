def calculate_average(numbers):
    # print(type(numbers))
    if not numbers:
        return None # Handle empty list
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    # print(sum([1,2]))
    # print(f'este es el tipo de la lista {type(list_to_iterate)}')
    # print(calculate_average(list_to_iterate))

    # Empty list: the function correctly handles an empty list by returnin None
    list_empty = []
    print(calculate_average(list_empty))
    '''
    None
    '''
    
    # Single element: Test with a list containing only one element
    list_one_element = [1]
    print(calculate_average(list_one_element))
    '''
    1.0
    '''
    
    '''
    Zero division: if the list contains only zeros, the division by len(numbers)
    would result in a ZeroDivisionerror. We could handle this by adding a check
    for the sum being zero
    '''
    list_zero_division = [0]
    print(calculate_average(list_zero_division))
    '''
    0.0
    '''
    
    '''
    Negative numbers: ensure the function works correctly with negative numbers
    '''
    list_negative = [-1, 3, -7, 24]
    print(calculate_average(list_negative))
    '''
    4.75
    '''
    
    '''
    Large numbers: Test with very large or very small numbers to check for
    potential overflow or underfolw issuess
    '''
    list_longest_shortest = [float('-inf'), float('inf')]
    print(calculate_average(list_longest_shortest))
    '''
    nan
    '''
    
    '''
    Non-numeric values: if the list contains non-numeric values, the sum
    function will raise a TypeError. we could handle this by using a try-except
    block or filtering out non-numeric values
    '''
    list_strings = ['zero', 'one', 'two']
    print(calculate_average(list_strings))
    '''
    Traceback (most recent call last):
    File "/home/drs/python302/cases/example.py", line 62, in <module>
        print(calculate_average(list_strings))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/drs/python302/cases/example.py", line 5, in calculate_average
        return sum(numbers) / len(numbers)
            ^^^^^^^^^^^^
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''