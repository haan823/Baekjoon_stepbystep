import sys

while True:
    l = list(map(int, sys.stdin.readline().split()))
    if l == [0, 0, 0]:
        break
    max_num = max(l)
    l.remove(max_num)
    result = 0
    for i in l:
        result += i ** 2
    if max_num ** 2 == result:
        print("right")
    else:
        print("wrong")
