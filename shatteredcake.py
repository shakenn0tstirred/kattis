W = int(input()) # Input total cake width
area = 0 #Initialize area

for i in range(int(input())): # area = length * width, so length = area/width; find the total area of the cake peices then divide by width to get length
    cake = input().split()
    area += int(cake[0]) * int(cake[1])

print(area//W) # The length is a whole number so // must be used
