n = int(input())
l = []
m = []
for i in range(n):
    l.append(input())
s = 0
for i, v in enumerate(l):
    m.append([])
    for j in v:
        if j not in m[i]:
            m[i].append(j)
            count = 1
        else:
            if m[i][-1] == j:
                count = 1
            else:
                count = 0
                break
    s += count
print(s)
