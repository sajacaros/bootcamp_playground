# https://leetcode.com/problems/shortest-path-in-binary-matrix
# 1091. Shortest Path in Binary Matrix
from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    row_len, col_len = len(grid), len(grid[0])

    visited = [[False] * col_len for _ in range(row_len)]
    direction = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1)]

    def is_valid(row, col):
        return 0 <= row < row_len and 0 <= col < col_len

    def bfs(start_row, start_col):
        q = deque()
        q.append((0, start_row, start_col))
        while q:
            depth, cur_r, cur_c = q.popleft()
            if (cur_r == (row_len - 1)) and (cur_c == (col_len - 1)):
                return depth + 1
            for r, c in direction:
                next_r, next_c = cur_r + r, cur_c + c
                if is_valid(next_r, next_c) and (grid[next_r][next_c] == 0) and visited[next_r][next_c] == False:
                    visited[next_r][next_c] = True
                    q.append((depth + 1, next_r, next_c))
        return -1

    if grid[0][0] != 0 or grid[row_len - 1][col_len - 1] != 0:
        return -1

    return bfs(0, 0)


grid = [ # 9
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0]
]
# grid = [[0]]
# grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [ # 4
#     [0,0,1,0],
#     [1,0,1,0],
#     [1,1,0,1],
#     [0,0,0,0]
# ]
# grid = [
#     [0,1],
#     [1,0]
# ]
print(shortestPathBinaryMatrix(grid))
