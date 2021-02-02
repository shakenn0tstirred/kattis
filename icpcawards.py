# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

winners = list()
rank = 0

for _ in range(int(input())):
    school,team = input().split()
    if school not in winners:
        print(school,team)
        winners.append(school)
        rank+=1
    if rank == 12:
        break
