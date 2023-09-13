# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    memo = [-1] * (len(cost)+2)
    new_cost = [0]
    new_cost.extend(cost)
    memo[0] = 0 # 0층
    memo[1] = 0 # 1층 가는 비용

    def min_cost(n): # n층가는 최소 비용
        if memo[n] >= 0:
            return memo[n]
        memo[n] = min(min_cost(n-2)+new_cost[n-2], min_cost(n-1)+new_cost[n-1])
        return memo[n]
    return min_cost(len(new_cost))

def minCostClimbingStairs2(cost: List[int]) -> int:
    cost.append(0)
    memo = [-1] * (len(cost)+1)
    memo[0] = cost[1] # 1층
    memo[1] = cost[2]

    def min_cost(n): # n층가는 최소 비용
        if memo[n] >= 0:
            return memo[n]
        memo[n] = min(min_cost(n-2), min_cost(n-1)) + cost[n]
        print(memo)
        return memo[n]
    return min_cost(len(cost)-1)

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] # 6
cost = [10,15,20] # 15
# cost = [0,0,0,1] #0
# cost = [1,0,0,1] #0
# cost = [0,1,0,1] # 0
print(minCostClimbingStairs2(cost))