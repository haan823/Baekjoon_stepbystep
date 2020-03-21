x = []
y = []
for i in range(3):
    x.append(int(input()))
for i in range(2):
    y.append(int(input()))
x.sort()
y.sort()
print(x[0] + y[0] - 50)
