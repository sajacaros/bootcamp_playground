import random

print(random.random()) # 0~1
arr = [3,4,7,1,2]
print(random.choice(arr)) # 주어진 리스트에서 1개 선택
print(random.sample(arr,2)) # 주어진 리스트에서 n개 선택
arr2 = arr.copy()
random.shuffle(arr2) # 리스트를 섞음
print(arr2)


def generate_lotto(nums):
    def wrapper():
        lotto_s = [i for i in range(1, 46)]
        ret = []
        for _ in range(nums):
            ret.append(random.sample(lotto_s, 6))
        return ret
    return wrapper

lotto_generator5 = generate_lotto(5)
print(lotto_generator5())





