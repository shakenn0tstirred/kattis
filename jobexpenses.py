# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

N = int(input())
budget = input().split()
expenses = 0

for i in range(N):
    if int(budget[i]) < 0:
        expenses += abs(int(budget[i]))
print(expenses)
