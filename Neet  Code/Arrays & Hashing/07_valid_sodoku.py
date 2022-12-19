import collections


def validSodoku(board: list[list[int]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            if (board[r][c] == rows[r] or
                board[r][c] == cols[c] or
                board[r][c] == squares[(r // 3),(c // 3)]):

                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3),(c // 3)].add(board[r][c])
