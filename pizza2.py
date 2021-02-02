# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Since pi cancels itself out, I don't use it in this program.

R,C = map(int, input().split())

if R == C:
   print(0)
else:
   answer = (R - C)**2
   answer /= R**2
   print(answer*100)
