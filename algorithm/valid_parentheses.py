import time
from typing import List


def is_valid(s: str) -> bool:
    parentheses = {']': '[', '}': '{', ')': '('}
    stack = []
    for c in s:
        if c in parentheses:
            ret = False
            while stack:
                cur = stack.pop()
                if cur == parentheses[c]:
                    ret = True
                    break
                elif cur in parentheses.values():
                    return False
            if not ret:
                return False
        else:
            stack.append(c)
    return not stack

def is_valid2(s: str) -> bool:
    parentheses = {']': '[', '}': '{', ')': '('}
    stack = []
    for c in s:
        if c in parentheses:
            if stack and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack



def time_trace(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        rt = func(*args, **kwargs)
        print(f'### time : {time.time() - st:.3f} ms')
        return rt

    return wrapper


@time_trace
def judge_test(solution, str, expected):
    result = solution(str)
    if not isinstance(result, bool):
        return False
    ret = (result == expected)
    if ret:
        print(f'success, func: {solution.__name__}, input: {str}')
        return True
    else:
        print(
            f'failed, func: {solution.__name__}, input: {str}, expect: {expected}, real: {result}')
        return False


def judge_helper(solution):
    assets = [
        ("{}", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("{", False),
        ("({[)", False),
        ("]", False),
        (")(){}", False),
    ]
    passed = sum([judge_test(solution, *asset) for asset in assets])
    print(f'{len(assets)} tests, passed : {passed}, failed: {len(assets) - passed}\n')


judge_helper(is_valid2)
