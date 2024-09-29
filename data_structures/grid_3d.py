from set_array import Array
import random

class Grid_3d:
    def __init__(self, rows, columns, depth):
        self.rows = rows # actually this works like depth
        self.columns = columns # actually this works like rows
        self.depth = depth # actually this works like cols
        
        self.data = Array(rows)
        
        for row in range(rows):
            self.data[row] = Array(columns)
            for column in range(columns):
                self.data[row][column] = Array(depth, None)
            
    
    def __str__(self):
        result = ''
        
        for row in range(self.rows):
            for col in range(self.columns):
                for d in range(self.depth):
                    result += str(self.data[row][col][d]) + ' '
                    
                result += '\n'
                
            result += '\n'
                    
        return str(result)
    
    def random_number_fill(self, lower_limit=0, higher_limit=10):
        for row in range(self.rows):
            for col in range(self.columns):
                for d in range(self.depth):
                    self.data[row][col][d] = random.randint(int(lower_limit), int(higher_limit))
            
            
if __name__ == '__main__':
    from grid_3d import Grid_3d
    
    matrix = Grid_3d(3,3,3)
    
    print(matrix.__str__())
    
    matrix_two = Grid_3d(4,3,3)
    matrix_two.random_number_fill()
    
    print(matrix_two)
