a = int(input())
b = int(input())
c = int(input())
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = list(str(a * b * c))
for i in range(10):
    for j in result:
        if i == int(j):
            l[i] += 1
for i in l:
    print(i)
