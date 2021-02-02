# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import factorial
for i in range(int(input())):
    print(factorial(int(input())) % 10) # takes the last digit of an integer
