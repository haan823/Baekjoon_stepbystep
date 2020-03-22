s = list(input().lower())
l = {}
for i in s:
    if i in l:
        l[i] += 1
    else:
        l[i] = 1
m = {}
for key, value in l.items():
    if value in m:
        m[value].append(key)
    else:
        m[value] = []
        m[value].append(key)
m = sorted(m.items(), reverse=True)
if len(m[0][1]) == 1:
    print(m[0][1][0].upper())
else:
    print("?")
