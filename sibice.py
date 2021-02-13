# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math

n, w, h = map(int, input().split())

for i in range(n):
  match = int(input())

  diagonal = math.sqrt(w**2 + h**2)

  if match > diagonal:
    print('NE')
  else:
    print('DA')
