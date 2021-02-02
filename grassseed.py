# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

cost = float(input())
answer = 0

for i in range(int(input())):
    width, length = map(float, input().split())
    answer += width * length * cost

print(answer)
