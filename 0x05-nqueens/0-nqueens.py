#!/usr/bin/python3
""" n queens """ 


def isSafe(board, row, col, n):
    """ check if a queen can be placed on board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col, n):
    """ recursive utility function to solve N Queen problem """
    if col == n:
        print([[i, row.index(1)] for i, row in enumerate(board)])
        return True
    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


def nqueens(n):
    """ n queens problem """
    board = [[0 for i in range(n)] for j in range(n)]
    if not solveNQUtil(board, 0, n):
        return False
    return True


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
