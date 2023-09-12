import time
from typing import List


def time_trace(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        rt = func(*args, **kwargs)
        print(f'### time : {time.time() - st:.3f} ms')
        return rt

    return wrapper


@time_trace
def judge_test(solution, nums, expected):
    result = solution(nums)
    ret = (result == expected)
    if ret:
        print(f'success, func: {solution.__name__}, input: {nums}')
    else:
        print(f'failed, func: {solution.__name__}, input: {nums}, expect: {expected}, real: {result}')


def judge_helper(solution):
    assets = [
        # nums, ret
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7)
    ]
    for asset in assets:
        judge_test(solution, *asset)


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    sorted_num = sorted(nums)
    prev = sorted_num[0]
    count, max_count = 1, 1
    for cur in sorted_num[1:]:
        if prev == cur:
            continue
        elif prev + 1 == cur:
            count += 1
        else:
            count = 1

        max_count = count if max_count < count else max_count
        prev = cur
    return max_count


# print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
judge_helper(longestConsecutive)
