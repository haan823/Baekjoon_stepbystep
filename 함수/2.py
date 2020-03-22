def dn(n):
    l = list(str(n))
    s = 0
    for i in l:
        s += int(i)
    s += n
    return s


m = []

for i in range(1, 10001):
    m.append(dn(i))

for i in range(1, 10001):
    if i not in m:
        print(i)
