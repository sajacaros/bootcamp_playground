import random

def generate_random_num(start=1, end=100):
    return random.randint(start, end)

answer = generate_random_num(1, 100)
for n in range(20):
    ask = int(input(f'{n+1} : 정답을 입력하세요 : '))
    if answer == ask:
        print(f"{answer} 정답입니다. {n+1}번째만에 맞추셨습니다.")
        break
    elif answer>ask:
        print(f"{ask} up")
    else:
        print(f"{ask} down")
else:
    print(f"정답을 못 맞추셨습니다. 정답은 {answer}입니다.")