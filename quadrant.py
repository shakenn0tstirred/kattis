# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Kattis-accepted code
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x > 0:
    print(4)
elif y > 0:
    print(2)
else:
    print(3)
    
    
# Simplified version utilizing the walrus operator introduced in Python 3.8

if (x:=int(input())) > 0 and (y:=int(input())) > 0:
    print(1)
elif x > 0:
    print(4)
elif y > 0:
    print(2)
else:
    print(3)
