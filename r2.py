# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

r1, answer = map(int, input().split())
# if R2/2 + R1/2 = answer, R2+R1 = 2*answer, and R2 = 2*answer - R1
r2 = (2*answer) - r1
print(r2)
