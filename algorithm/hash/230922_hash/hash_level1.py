def solution(participant, completion):
    p_hash = {}
    for p in participant:
        p_hash[p] = p_hash[p]+1 if p in p_hash else 1
    for c in completion:
        if c in p_hash and p_hash[c] == 1:
            p_hash.pop(c)
        elif c in p_hash:
            p_hash[c] -= 1

    return p_hash.popitem()[0]