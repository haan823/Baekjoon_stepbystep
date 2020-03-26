n = int(input())
min_num = n

for i in range(1, n):
    l = list(str(i))
    sum = 0
    for j in l:
        sum += int(j)
    if sum + i == n and i < min_num:
        min_num = i
if min_num == n:
    print(0)
else:
    print(min_num)
