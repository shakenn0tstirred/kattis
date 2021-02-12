# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for num in range(int(input()),1000000001):
    harshad = 0
    for digit in str(num):
        harshad += int(digit)
    if num % harshad == 0:
        print(num)
        break
