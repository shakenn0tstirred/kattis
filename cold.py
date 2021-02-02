# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

n = (int, input().split()) # Input number of temperatures
tempList = list(map(int, input().split())) # Input list of temperatures
t = sum(1 for number in tempList if number < 0) # Add the temperatures below zero to the running total
print(t) # Print number of subzero temperatures
