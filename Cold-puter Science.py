n = (int, input().split()) # Input number of temperatures
tempList = list(map(int, input().split())) # Input list of temperatures
t = sum(1 for number in tempList if number < 0) # Add the temperatures below zero to the running total
print(t) # Print number of subzero temperatures
