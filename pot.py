# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

answer = 0 # Initialize answer and power variable
power = 0

#Loop through the number of test cases
for i in range(int(input())):
    num = input()
    power = num[-1] # The last character is what we want for the power
    num = num[:-1] # Remove the last character from the original string
    answer += int(num)**int(power) # Cast both elements as int, keep running total of the sums of powers

print(answer)
