c = int(input())
l = []
avg = []
for i in range(c):
    l.append(list(map(int, input().split())))
for i, v1 in enumerate(l):
    s = 0
    length = 0
    for j, v2 in enumerate(l[i]):
        if j == 0:
            continue
        else:
            s += v2
            length += 1
    avg.append(s / length)
for i, v1 in enumerate(l):
    count = 0
    for j, v2 in enumerate(l[i]):
        if j == 0:
            continue
        else:
            if v2 > avg[i]:
                count += 1
    print("%.3f" % round(((count / (len(l[i]) - 1)) * 100), 3), end="")
    print("%")
