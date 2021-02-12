# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

seedlings = int(input()) # Accept first line of code, the number of seedlings to be planted
days = [int(x) for x in input().split()] # Cast each seedling maturity dates to int

days.sort(reverse = True) # Sort seedling list from longest to shortest
total_days = list() # Initialize a list to catalogue maximum growth times

for i in range(seedlings):
    total_days.append(i+days[i]+2)

print(max(total_days))
