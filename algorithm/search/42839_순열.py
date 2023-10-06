# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def solution(numbers):
    prime_dict = {0: False, 1: False}

    def is_prime_number(x):
        if x in prime_dict:
            return prime_dict[x]

        for i in range(2, x):
            if x % i == 0:
                prime_dict[x] = False
                return False
        prime_dict[x] = True
        return True

    def permutations_set(num_s_list):
        p_set = set()
        for p_l in range(1, len(num_s_list) + 1):
            for p in permutations(num_s_list, p_l):
                ret = ''
                for p in p:
                    ret += p
                p_set.add(int(ret))
        return p_set

    nums = [n for n in numbers]
    perm = permutations_set(nums)
    print(perm)

    answer = 0
    for c in perm:
        # print(c, ' is prime : ', is_prime_number(c))
        if is_prime_number(c):
            answer += 1

    return answer

# print(solution("17"))
print(solution("011"))