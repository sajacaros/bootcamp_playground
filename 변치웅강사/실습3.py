from functools import reduce

def sum(arr: []) -> int:
    return reduce(lambda acc, cur: acc + cur, arr, 0)


def input_and_sum() -> tuple[list[int], int]:
    nums_str = input('숫자 5개를 입력하세요.(ex> 3,4,5,6,7) : ')
    nums = list(map(int, nums_str.split(',')))
    return nums, sum(nums)


in_value, out_value = input_and_sum()
print(f'{in_value} sum : {out_value}')

def func(x, y, z=1, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(z), z)
    print(type(args), args)
    print(type(kwargs), kwargs)

func(1, 2, 3, 4, 5, l=3, k=4)