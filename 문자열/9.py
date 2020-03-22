s = input()
count = 0
l = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in l:
    while True:
        if i in s:
            count += 1
            s = s.replace(i, " ", 1)
        else:
            break
for i in s:
    if i != " ":
        count += 1
print(count)
