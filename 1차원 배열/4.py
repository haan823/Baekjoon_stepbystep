l = []
for i in range(10):
    l.append(int(input()))
for i, v in enumerate(l):
    l[i] = v % 42
l = list(set(l))
print(len(l))
