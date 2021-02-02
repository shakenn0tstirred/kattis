# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Determines whether the input is even or odd
for i in range(int(input())):
    x = int(input())
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")
