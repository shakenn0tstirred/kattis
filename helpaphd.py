# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for i in range(int(input())):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        a,b = line.split('+') # .split() defaults to splitting a string at a space, so split the line at the plus sign
        print(int(a) + int(b)) # Output the added numbers
