from set_array import Array
import random

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + ' '
                
            result += '\n'
                
        return str(result)
    
                
    def random_number_fill(self, lower_limit=0, higher_limit=10):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self[row][column] = random.randint(int(lower_limit), int(higher_limit))
                
        return self
        
    def random_letters_fill(self):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self[row][column] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
        return self
            
    def random_string_fill(self):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self[row][column] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        
        return self
    
if __name__ == '__main__':
    from grid import Grid
    
    matrix = Grid(3, 3)
    print(matrix.__str__())

    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column
            
    print(matrix)
    
    print(matrix.get_height())
    # 3
    
    print(matrix.get_width())
    # 3
    
    print(matrix.__getitem__(1))
    # [0, 1, 2]
    
    print(matrix.__getitem__(1)[2])
    # 2
    
    print(matrix.__str__())
    
    '''
    0 0 0 
    0 1 2 
    0 2 4 
    '''
    
    matrix_two = Grid(3, 3)
    print(f'this the matrix two: \n{matrix_two}')
    
    '''
    this the matrix two: 
    None None None 
    None None None 
    None None None 
    '''
    
    print(f'this the matrix two filled with numbers: \n{matrix_two.random_number_fill()}')
    
    print(f'this the matrix two filled with letters: \n{matrix_two.random_letters_fill()}')
    
    print(f'this the matrix two filled with numbers and/ or letters as strings: \n{matrix_two.random_string_fill()}')

    


    
