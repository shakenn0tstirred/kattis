cost = float(input())
L = int(input())
answer = 0

for i in range(L):
    width, length = map(float, input().split())
    answer += width * length * cost

print(answer)
