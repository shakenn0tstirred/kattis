# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

answer = 0 # Initialize answer variable
for i in range(int(input())): # Loop through number of life periods
    q, y = map(float, input().split())
    answer += q * y # Keep a running total of the quantity of life periods
print(answer)
