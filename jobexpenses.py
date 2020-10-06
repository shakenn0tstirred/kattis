N = int(input())
budget = input().split()
expenses = 0

for i in range(N):
    if int(budget[i]) < 0:
        expenses += abs(int(budget[i]))
print(expenses)
