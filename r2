r1, answer = map(int, input().split())
# if R2/2 + R1/2 = answer, R2+R1 = 2*answer, and R2 = 2*answer - R1
r2 = (2*answer) - r1
print(r2)
