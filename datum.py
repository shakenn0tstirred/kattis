# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from calendar import weekday

D,M = map(int, input().split())
answer = weekday(2009,M,D)
if answer == 0:
    answer = "Monday"
elif answer == 1:
    answer = "Tuesday"
elif answer == 2:
    answer = "Wednesday"
elif answer == 3:
    answer = "Thursday"
elif answer == 4:
    answer = "Friday"
elif answer == 5:
    answer = "Saturday"
else:
    answer = "Sunday"

print(answer)
