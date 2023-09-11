from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    len_n = len(nums)
    for i in range(len_n):
        for j in range(i+1, len_n):
            if nums[i]+nums[j] == target:
                return [i, j]

def twoSum2(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for idx, n in enumerate(nums):
        num_dict[n] = idx

    for idx, n in enumerate(nums):
        diff = target - n
        if diff in num_dict and idx != num_dict[diff]:
            return [idx, diff]

def judge_test(solution, nums, target, expected):
    ret = (solution(nums, target).sort() == expected.sort())
    if ret:
        print(f'success, input:{nums}, target:{target}')
    else:
        print(f'failed, input:{nums}, target:{target}, expect : {expected}, real : {ret}')

def judge_tests(solution):
    assets = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 3, 5, 6, -10, 3, 10], 0, [4, 6])
    ]
    for asset in assets:
        judge_test(solution, *asset)

judge_tests(twoSum)
judge_tests(twoSum2)