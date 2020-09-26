import math
answer = 0
h, v = map(int, input().split())

answer = h / math.sin(math.radians(v)) # height / sin(v) = ladder length
print(math.ceil(answer)) # Round the answer up to the nearest whole number
