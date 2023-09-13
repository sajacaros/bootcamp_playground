# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths
def uniquePaths(m: int, n: int) -> int:
    memo = [[0]*n for _ in range(m)]
    def dfs(i, j):
        if i == 1 or j == 1:
            return 1
        if memo[i-1][j-1] == 0:
            memo[i-1][j-1] = dfs(i-1, j) + dfs(i, j-1)
        return memo[i-1][j-1]
    return dfs(m, n)


def uniquePaths2(m: int, n: int) -> int:
    memo = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[m-1][n-1]

def uniquePaths_basic(m, n):
    memo = [[-1] * n for _ in range(m)]

    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1
    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    return memo[m-1][n-1]

print(uniquePaths_basic(1,3))