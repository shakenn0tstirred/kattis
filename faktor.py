A, I = map(int, input().split())

if A == 1:
    print(I)
else:
    I -= 1
    print(A * I + 1)
