answer = 0 # Initialize answer variable
for i in range(int(input())): # Loop through number of life periods
    q, y = map(float, input().split())
    answer += q * y # Keep a running total of the quantity of life periods
print(answer)
