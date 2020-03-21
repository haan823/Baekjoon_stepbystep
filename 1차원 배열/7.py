c = int(input())
l = []
avg = []
for i in range(c):
    l.append(list(map(int, input().split())))
for i, v1 in enumerate(l):
    sum = 0
    len = 0
    for j, v2 in enumerate(l[i]):
        if j == 0:
            continue
        else:
            sum += v2
            len += 1
    avg.append(sum / len)
print(l)
print(avg)
for i, v1 in enumerate(l):
    count = 0
    for j, v2 in enumerate(l[i]):
        if j == 0:
            continue
        else:
            if v2 > avg[i]:
                count += 1
    print(count)
    print(len(l[i]))
