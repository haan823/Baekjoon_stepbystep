n = int(input())
l = list(map(int, input().split()))
max_num = max(l)
for i, v in enumerate(l):
    l[i] = (v / max_num) * 100
print(sum(l) / len(l))
