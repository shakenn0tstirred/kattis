N = int(input()) # Input number of test cases
answer = 0 # Initialize answer and power variable
power = 0

#Loop through the number of test cases
for i in range(N):
    num = input()
    power = num[-1] # The last character is what we want for the power
    num = num[:-1] # Remove the last character from the original string
    answer += int(num)**int(power) # Cast both elements as int, keep running total of the sums of powers

print(answer)
