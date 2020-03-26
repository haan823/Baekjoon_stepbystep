n, m = map(int, input().split())
l = list(map(int, input().split()))

max_num = 0

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            if (l[i] + l[j] + l[k]) <= m and (l[i] + l[j] + l[k]) > max_num:
                max_num = l[i] + l[j] + l[k]

print(max_num)
