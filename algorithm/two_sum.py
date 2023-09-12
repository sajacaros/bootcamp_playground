import time
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    len_n = len(nums)
    for i in range(len_n):
        for j in range(i + 1, len_n):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum_dict(nums: List[int], target: int) -> List[int]:
    num_dict = {idx:num for idx, num in enumerate(nums)}
    len_n = len(nums)
    for i in range(len_n):
        for j in range(i + 1, len_n):
            if num_dict[i] + num_dict[j] == target:
                return [i, j]


def twoSum2(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for idx, n in enumerate(nums):
        num_dict[n] = idx

    for idx, n in enumerate(nums):
        diff = target - n
        if diff in num_dict and idx != num_dict[diff]:
            return [idx, num_dict[diff]]


def time_trace(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        rt = func(*args, **kwargs)
        print(f'### time : {time.time() - st:.3f} ms')
        return rt

    return wrapper


@time_trace
def judge_test(solution, nums, target, expected):
    result = solution(nums, target)
    ret = (sorted(result) == sorted(expected))
    if ret:
        print(f'success, func: {solution.__name__}, input: {nums}, target: {target}')
    else:
        print(f'failed, func: {solution.__name__}, input: {nums}, target: {target}, expect: {expected}, real: {result}')


def judge_helper(solution):
    assets = [
        # nums, target, ret
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 3, 5, 6, -10, 3, 10], 0, [4, 6])
    ]
    for asset in assets:
        judge_test(solution, *asset)


judge_helper(twoSum)
judge_helper(twoSum2)
judge_helper(twoSum_dict)