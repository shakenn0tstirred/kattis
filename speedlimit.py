n = int(input())

while n != -1:
    time = 0
    distance = 0

    for i in range(n):
        mph,h = map(int, input().split())
        distance += (h - time) * mph
        time = h
    print(distance, "miles")
    n = int(input())
