n = int(input())

# Determines whether the input is even or odd
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")
