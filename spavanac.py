# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

h,m = map(int, input().split())

if m - 45 < 0:
    m += 15 # 60 - 45 = 15, so add 15 if m-45 is negative
    h -= 1
    if h < 0:
        h = 23
else:
    m -= 45
