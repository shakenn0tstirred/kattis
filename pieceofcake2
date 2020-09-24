# Brute force solution, making all possible combinations of the cake's 2 cuts (with a height of 4 cm)

n, h, v = map(int, input().split())

cake = []
cake.append(h * v * 4)
cake.append((n - h) * v * 4)
cake.append(h * (n - v) * 4)
cake.append((n - h) * (n - v) * 4)

print(max(cake))
