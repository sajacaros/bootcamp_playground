# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    pattern_1 = [1,2,3,4,5,]
    pattern_2 = [2,1,2,3,2,4,2,5,]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5,]

    same_count= [0, 0, 0]
    for idx, n in enumerate(answers):
        if pattern_1[idx % len(pattern_1)] == n:
            same_count[0] += 1
        if pattern_2[idx % len(pattern_2)] == n:
            same_count[1] += 1
        if pattern_3[idx % len(pattern_3)] == n:
            same_count[2] += 1

    max_ = max(same_count)
    for idx, s in enumerate(same_count):
        if s == max_:
            answer.append(idx+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))