class Solution:
    # create a set for each row, col, and box to track what we've seen
    def isValidSudoku(self, board):
        n = len(board)
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        for i in range(3):
            for j in range(3):
                boxes[(i,j)] = set()
 # iterate through every cell in the 9x9 grid
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                
            # skip empty cells, they can't cause duplicates
                if val == ".":
                    continue
                
                if val in rows[row]: return False
                if val in cols[col]: return False
                if val in boxes[(row//3, col//3)]: return False  # row//3 and col//3 tells us which box we're in (0,1, or 2)
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[(row//3, col//3)].add(val)
        
        return True