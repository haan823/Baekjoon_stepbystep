l = []
max_value = 0
for i in range(9):
    l.append(int(input()))
for i, v in enumerate(l):
    if v > max_value:
        index = i + 1
        max_value = v
print(max_value)
print(index)

