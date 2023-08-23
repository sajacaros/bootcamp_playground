# map
items = [' 로지텍마우스 ', ' 앱솔 키보드 ', ' ms 마우스 ']

def str_strip(s):
    return s.strip()
print(list(map(str_strip, items)))

print(list(map(lambda s: s.strip(), items)))


# filter
nums = [-3, 2, 1, 10, -3, 0]

def is_positive(n):
    return n > 0
print(list(filter(is_positive, nums)))

print(list(filter(lambda s: s > 0, nums)))
