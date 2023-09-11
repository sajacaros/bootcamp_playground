import time
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    # [73, 74, 75, 71, 69, 72, 76, 73],
    # [ 1,  1,  4,  2,  1,  1,  0,  0]
    ret = [0]*len(temperatures)
    for i, t in enumerate(temperatures):
        for j, t2 in enumerate(temperatures[i:]):
            if t < t2:
                ret[i]=j
                break
    return ret


def daily_temperatures_stack(temperatures: List[int]) -> List[int]:
    # [73, 74, 75, 71, 69, 70, 76, 73],
    # [ 1,  1,  4,  3,  1,  1,  0,  0]
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for d, t in enumerate(temperatures):
        while stack and stack[-1][1] < t:
            prev_d = stack.pop()[0]
            answer[prev_d] = d - prev_d
        stack.append((d, t))
    return answer


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
        return True
    else:
        print(
            f'failed, func: {solution.__name__}, input: {nums}, expect: {expected}, real: {result}')
        return False

def judge_helper(solution):
    assets = [
        # temperatures, wait
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [ 1,  1,  4,  2,  1,  1,  0,  0]
        ),
        (
            [73, 74, 75, 71, 69, 70, 76, 73],
            [ 1,  1,  4,  3,  1,  1,  0,  0]
        ),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90],  [1, 1, 0]),
    ]
    passed = sum([judge_test(solution, *asset) for asset in assets])
    print(f'{len(assets)} tests, passed : {passed}, failed: {len(assets) - passed}\n')


judge_helper(daily_temperatures)
judge_helper(daily_temperatures_stack)
judge_helper(daily_temperatures_stack2)
