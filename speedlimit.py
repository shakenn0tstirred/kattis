# Kattis-accepted implementation

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

    
# Simplify code by implementing the walrus operator in Python 3.8+

while (n:=int(input())) != -1:
    time = 0
    distance = 0

    for i in range(n):
        mph,h = map(int, input().split())
        distance += (h - time) * mph
        time = h
    print(distance, "miles")
