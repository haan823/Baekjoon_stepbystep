l = []
for i in range(1, 6):
    score = int(input())
    if score >= 40:
        l.append(score)
    else:
        l.append(40)
sum = 0
count = 0
for i in l:
    sum += i
    count += 1
print(sum // count)
