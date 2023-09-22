def solution(phone_book):
    num_hash = {}
    for idx in range(1, len(phone_book)):
        target = phone_book[idx - 1]
        for s_i in range(len(target)-1):
            if target[:s_i + 1] in num_hash:  # 이미 앞 번호가 안 되므로 더이상 조회 불필요
                num_hash[target[:s_i + 2]] = True
        if target not in num_hash:
            for n in phone_book[idx:]:
                if target == n[:len(target)]:
                    return False
            num_hash[target] = True
    return True
