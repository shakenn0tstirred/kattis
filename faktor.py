# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

A, I = map(int, input().split())

if A == 1:
    print(I)
else:
    I -= 1
    print(A * I + 1)
