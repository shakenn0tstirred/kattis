from math import sin, radians, ceil
answer = 0
h, v = map(int, input().split())

answer = h / sin(radians(v)) # height / sin(v) = ladder length
print(ceil(answer)) # Round the answer up to the nearest whole number
