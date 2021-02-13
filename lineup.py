# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

names = list()
for i in range(int(input())):
  names.append(input())

sorted_names = sorted(names)
rev_sorted_names = sorted(names,reverse = True)

if names == sorted_names:
  print("INCREASING")
elif names == rev_sorted_names:
  print("DECREASING")
else:
  print("NEITHER")
