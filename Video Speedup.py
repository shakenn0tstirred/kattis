n, p, k = map(int, input().split())
t = list(map(int, input().split()))

p /= 100
i = 0
T = t[i]
j = i + 1

if t[i] == k or p == 0 or p == 100:
    pass
else:
    while j < n:
        T = T + (1 + p*j) * (t[j] - t[i])
        i+=1
        j+=1

T = T + (1 + p*j) * (k - t[i])
print(T)
