def solution(phone_book):
    hash_book = {phone:True for phone in phone_book}
    for phone in phone_book:
        for s_idx in range(len(phone)-1):
            if phone[:s_idx+1] in hash_book:
                return False
    return True
