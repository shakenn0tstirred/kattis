# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for i in range(int(input())):
    r, e, c = map(int, input().split())

    cost = e - c
    if r < cost:
        print("advertise")
    elif r > cost:
        print("do not advertise")
    else:
        print("does not matter")
