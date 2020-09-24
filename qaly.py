num_life_periods = int(input()) # Input number of life periods
answer = 0 # Initialize answer variable
for i in range(num_life_periods):
    q, y = map(float, input().split())
    answer += q * y # Keep a running total of the quantity of life periods
print(answer)
