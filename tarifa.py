# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

X = int(input())
data = 0

for i in range(int(input())):
    data += X - int(input())

print(data+X)
