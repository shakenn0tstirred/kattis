##f(0) = 2
##f(x) = 2 * f(x-1) - 1

iterations = int(input())
answer = 2

for i in range(iterations):
    answer = 2 * answer - 1

print(answer**2)
