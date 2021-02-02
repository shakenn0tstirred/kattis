# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import sin, radians, ceil
answer = 0
h, v = map(int, input().split())

answer = h / sin(radians(v)) # height / sin(v) = ladder length
print(ceil(answer)) # Round the answer up to the nearest whole number
