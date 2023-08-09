class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        test = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
        row_len, col_len = len(board), len(board[0])
        
        def backtracking(pro, r, c, index):
            if pro == word:
                return True
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or index == len(word):
                return False

            if board[r][c] != word[index]:
                return False
            
            if test[r][c] and board[r][c] == word[index]:
                test[r][c] = False
                if backtracking(pro + board[r][c], r + 1, c, index + 1) or \
                   backtracking(pro + board[r][c], r - 1, c, index + 1) or \
                   backtracking(pro + board[r][c], r, c + 1, index + 1) or \
                   backtracking(pro + board[r][c], r, c - 1, index + 1):
                    return True
                test[r][c] = True
            
            return False
        
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == word[0]: 
                    if backtracking("", r, c, 0):
                        return True
                    
        return False
