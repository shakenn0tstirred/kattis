# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

days = []

for i in range(int(input())):
    s,t = map(int,input().split()) # Get two dates
    days += range(s,t+1) # Add covered dates to list
print(len(set(days))) #Sets remove duplicates, so print number of non-duplicate days
