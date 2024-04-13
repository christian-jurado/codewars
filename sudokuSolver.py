def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    # 1st corner case where there are no empty cells (0), sudoku is done.
    # 2nd need to put numbers from 1-9 in the empty cells (0), 
    # to know the coordinates of the empty cell need to find the coordinates of the empty cells.
    # 3rd Have to call recursively the function to fill the sudoku
    # if the solution doesn't solve the sudoku must return the 
    # original numbers (return to 0 the numbers that were substituded).
    
    empty_cell = find_empty_cell(puzzle)    
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_num(puzzle, row, col, num):
            puzzle[row][col] = num
            
            if sudoku(puzzle):
                return puzzle

            puzzle[row][col] = 0

    return False

def find_empty_cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def is_valid_num(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) 
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if puzzle[i][j] == num:
                return False
            
    return True

print(sudoku([[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]))