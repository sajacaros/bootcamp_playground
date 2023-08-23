balance = 0
while True:
    msg = '''
    안녕하세요 AI 은행입니다. 원하시는 서비스 메뉴를 입력 해주세요.
    1. 입금
    2. 출금
    3. 잔액 확인
    4. 종료
    '''
    print(msg)

    menu = int(input('원하시는 서비스 메뉴를 숫자로 입력해주세요. : '))

    if menu == 1:
        money = int(input('입금할 금액을 입력해 주세요. : '))
        balance += money
        print(f"{money}를 입금했습니다. 잔액은 {balance}입니다.")
    elif menu == 2:
        money = int(input('입금할 금액을 입력해 주세요. : '))
        if money > balance:
            print('입금할 금액이 잔고보다 큽니다. 다시 입력해 주세요.')
            continue
        balance -= money
        print(f"{money}를 출금했습니다. 잔액은 {balance}입니다.")
    elif menu == 3:
        print(f"잔액은 {balance}입니다.")
    elif menu == 4:
        print('이용해 주셔서 감사합니다.')
        break
    else:
        print('지원하지 않는 메뉴 숫자입니다. 다시 입력해 주세요.')