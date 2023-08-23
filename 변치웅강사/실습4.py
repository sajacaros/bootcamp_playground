import time
import random


def descript_bmi(bmi: float):
    if bmi < 20:
        print(f"bmi - {bmi}은 저체중입니다.")
    elif bmi < 24:
        print(f"bmi - {bmi}은 표준체중입니다.")
    elif bmi < 30:
        print(f"bmi - {bmi}은 과체중입니다.")
    else:
        print(f"bmi - {bmi}은 비만입니다.")


def bmi(weight: float, height: float) -> int:
    return int(weight / (pow(height / 100, 2) + 1e-4))


# weight = float(input("체중을 입력해 주세요 - "))
# height = float(input("키를 입력해 주세요 - "))
# descript_bmi(bmi(weight, height))

from functools import reduce
def sum_sum(arr):
    return reduce(lambda a, b: a + b, arr, 0)

# print(sum_sum([1, 2, 3]))

def spending_time(display_name=''):
    def wrapper2(func):
        def wrapper(*arg, **kwargs):
            start = time.time()
            ret = func(*arg, **kwargs)
            end = time.time()
            print(f"({display_name})'s 소비시간은 {end-start} 입니다.")
            return ret
        return wrapper
    return wrapper2

@spending_time(display_name='reduce max')
def max_max(arr):
    return reduce(lambda a, b: a if a > b else b, arr[1:], arr[0])

@spending_time(display_name='for max')
def max_max2(arr):
    max = arr[0]
    for n in arr[1:]:
        if n>max:
            max = n
    return max

@spending_time(display_name='sort max')
def max_max3(arr):
    arr.sort()
    return arr[-1]

n = 1_000_000
test_list = [random.randint(0, n) for _ in range(n)]
print(test_list[0:10])
print(max_max(test_list))
print(max_max2(test_list))
print(max_max3(test_list))
