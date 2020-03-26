n = int(input())
l = [666]

i = 1666

while n:
    if "666" in str(i):
        l.append(i)
    if len(l) == 10001:
        break
    i += 1

print(l[n - 1])
