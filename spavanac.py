h,m = map(int, input().split())

if m - 45 < 0:
    m += 15 # 60 - 45 = 15, so add 15 if m-45 is negative
    h -= 1
    if h < 0:
        h = 23
else:
    m -= 45
