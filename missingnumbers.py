good_job = True
numbers = list()

n = int(input())

for i in range(1,n+1):
    numbers.append(int(input()))

for j in range(1,numbers[-1]):
    if j not in numbers:
        print(j)
        good_job = False

if good_job:
    print("good job")
