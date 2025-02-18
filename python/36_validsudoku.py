class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create hashmap for row
        cols = collections.defaultdict(set)
        #create hashmap for column
        rows = collections.defaultdict(set)
        #create a hashmap for 3x3
        squares = collections.defaultdict(set)


        for r in range(len(board)):
            for c in range(len(r)):
                if board[r][c] == ".":
                    continue
                if  (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3,c//3]
                    ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])     
        return True
        