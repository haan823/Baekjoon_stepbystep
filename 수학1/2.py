n = int(input())
count = []

for i in range((n // 5) + 1):
    for j in range((n // 3) + 1):
        if n == (5 * i) + (3 * j):
            count.append(i + j)
        else:
            continue

if count:
    print(min(count))
else:
    print(-1)
