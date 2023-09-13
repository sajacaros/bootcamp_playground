from collections import deque
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def bfs(row, col):


    count = 0
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in m]
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "1" and visited[row][col] == False:
                bfs(row, col)
                count += 1

    return count



i1 =   [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(i1)) # 1