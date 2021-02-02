# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

answer = 0
for _ in range(int(input())):
    color = input()

    if "rose" in color.lower() or "pink" in color.lower():
        answer+=1

if answer == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(answer)
