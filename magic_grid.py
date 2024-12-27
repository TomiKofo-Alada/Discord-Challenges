# a magic square is a grid where the sums of the numbers in
# each row, column, and both diagonals are equal. for a 3*3
# magic square, this sum is known as the magic constant.
# your task is to check if a given 3*3 grid is a valid magic square. 

def magic_grid(grid):
    # define the magic constant for a 3x3 magic square
    magic_constant = 15
    
    # check if grid has all numbers from 1 to 9 exactly once
    numbers = [num for row in grid for num in row]
    if sorted(numbers) != list(range(1,10)):
        return False
    
    # check rows and colum
    for i in range(3):
        if sum(grid[i]) != magic_constant: # check row i
            return False
        if sum(row[i] for row in grid) != magic_constant:  # check column
            return False
        
    # check diagonals
    if (grid[0][0] + grid[1][1] + grid[2][2] != magic_constant) or \
        (grid[0][2] + grid[1][1] + grid[2][0] != magic_constant):
            return False
        
    return True