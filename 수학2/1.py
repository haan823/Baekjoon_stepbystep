n = int(input())
l = list(map(int, input().split()))
result = 0
for i in l:
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
        else:
            continue
    if count == 2:
        result += 1
print(result)
