# age = int(input('나이를 입력해 주세요. '))

# age_level = '성인' if age>18 else '미성년자'
# print(age_level)

# nums = [1,2,3,4,5,6,7,8,9,10]
# print([n for n in nums if n>3])

from functools import reduce


scores = {
    'Kim': {'math': 50, 'english': 70},
    'Park': {'math': 70, 'english': 60},
    'Lee': {'math': 80, 'english': 50}
}

# 영어의 총합
sum_ret = 0
for key in scores.keys():
    sum_ret += scores[key]['english']
print(f'sum : {sum_ret}')


# 수학 점수가 60점 이상인 사람 뽑기
students = [
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
]
print([s for s in students if s['score']['math']>=60])


# 학생별 점수 총합
for student in students:
    total = 0
    for score in student['score'].values():
        total += score
        print(f'total : {total}')


for student in students:
    print(f"total : {sum(student['score'].values())}")


def print_str(*args):
    print(args)
    print(*args)

print_str('args test')

students = [{'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
            {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
            {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
            {'id': 4, 'name': 'Choi', 'score': {'math': 70, 'english': 50}}]

def total_score(*args):
    return sum([sum(student['score'].values()) for student in args])

print(f'total score : {total_score(*students)}')


def reverse(acc, cur):
    print(f'acc : {acc}')
    print(f'cur : {cur}')
    return [cur, *acc]
print(reduce(lambda acc, cur: [cur, *acc], [1,2,3], []))
print(reduce(reverse, [1,2,3], []))

students = [
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70, 'science': 60}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60, 'science': 100}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50, 'science': 40}},
]
# reduce를 이용해 모든 점수의 총합 리턴
total = 0
for s in students:
    print(s['score'].values())
    total += reduce(lambda acc,cur: acc+cur, s['score'].values(), 0)
print(f'total : {total}')

print(f"total : {reduce(lambda acc, cur: acc + sum(cur['score'].values()), students, 0)}")
