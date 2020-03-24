import sys

l_x = []
l_y = []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    l_x.append(x)
    l_y.append(y)
count_x = {}
count_y = {}
a = l_x[0]
b = l_y[0]
for i in l_x:
    try:
        count_x[i] += 1
    except:
        count_x[i] = 1
for i in l_y:
    try:
        count_y[i] += 1
    except:
        count_y[i] = 1
for key, value in count_x.items():
    if value == 1:
        print(key, end=" ")
for key, value in count_y.items():
    if value == 1:
        print(key)
