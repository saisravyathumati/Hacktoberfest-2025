def is_valid_sudoku(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                if (i, num) in seen or (num, j) in seen or (i//3, j//3, num) in seen:
                    return False
                seen.update({(i, num), (num, j), (i//3, j//3, num)})
    return True

if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Sudoku valid:", is_valid_sudoku(board))
