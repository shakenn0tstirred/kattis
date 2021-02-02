# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

X, Y, N = map(int, input().split())

for i in range(1, N+1):
    if i % X == 0 and i % Y == 0:
        print("FizzBuzz")
    elif i % X == 0:
        print("Fizz")
    elif i % Y == 0:
        print("Buzz")
    else:
        print(i)
