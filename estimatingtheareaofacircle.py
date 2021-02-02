# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import pi
line = input().split()

while line != ['0', '0', '0']:
    r = float(line[0])
    m = int(line[1])
    c = int(line[2])
    d = 2 * r

    print(pi*r**2,(c/m)*d**2)
    
    line = input().split()
