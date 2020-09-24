import math # Need math library for factorial operation
test_cases = int(input()) # Input number of test cases
for i in range(test_cases):
    num = math.factorial(int(input())) % 10 # takes the last digit of an integer
    print(num)
