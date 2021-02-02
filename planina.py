# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

##f(0) = 2
##f(x) = 2 * f(x-1) - 1

answer = 2
for i in range(int(input())):
    answer = 2 * answer - 1

print(answer**2)
