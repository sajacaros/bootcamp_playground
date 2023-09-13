# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs


# 1 1 - 1
# 2 11 2 - 2
# 3 111 12 21 - 3
# 4 1111 112 121 211 22 - 5
# 5 11111 1211 1121 1112 122 212 221 2111- 8

memo = {1: 1, 2: 2}


def climbStairs(n: int) -> int:
    if n in memo:
        return memo[n]
    memo[n] = climbStairs(n - 1) + climbStairs(n - 2)
    return memo[n]

def climbStairs2(n: int) -> int:
    memo = {1:1, 2:2}
    for i in range(3,n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n-1]+memo[n-2]

print(climbStairs(44))  # 1134903170
print(climbStairs2(44))  # 1134903170
