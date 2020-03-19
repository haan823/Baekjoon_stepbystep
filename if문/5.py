h, m = map(int, input().split())
if h > 0:
    if m >= 45:
        print(f"{h} {m-45}")
    elif m < 45:
        print(f"{h-1} {m+15}")
elif h == 0:
    if m >= 45:
        print(f"{h} {m-45}")
    elif m < 45:
        print(f"23 {m+15}")
