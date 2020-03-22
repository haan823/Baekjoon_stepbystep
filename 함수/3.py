def han(n):
    l = list(str(n))
    if len(l) == 1 or len(l) == 2:
        return 1
    elif len(l) >= 3:
        for i in range(2, len(l)):
            if int(l[0]) - int(l[1]) == int(l[i - 1]) - int(l[i]):
                continue
            else:
                return 0
        return 1


count = 0
for i in range(1, int(input()) + 1):
    if han(i) == 1:
        count += 1
print(count)
