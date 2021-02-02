# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

left, right = map(int, input().split())

if left == right == 0:        # This catches the no-tined moose
    print("Not a moose")
elif left == right:           # This catches even-sided moose
    total = str(left + right)
    print("Even " + total)
elif left > right:            # Catches moose with more tines on the left than right
    total = str(2 * left)
    print("Odd " + total)
else:                         # Catches moose with more right tines than left; else statement is slightly more minimal
    total = str(2 * right)
    print("Odd " + total)
