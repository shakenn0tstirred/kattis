n = (int, input().split())
tempList = list(map(int, input().split()))
t = sum(1 for number in tempList if number < 0)
print(t)
