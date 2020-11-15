cost = float(input())
answer = 0

for i in range(int(input())):
    width, length = map(float, input().split())
    answer += width * length * cost

print(answer)
