# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Kattis-accepted implementation
n = int(input())

while n != -1:
    time = 0
    distance = 0

    for i in range(n):
        mph,h = map(int, input().split())
        distance += (h - time) * mph
        time = h
    print(distance, "miles")
    n = int(input())

    
# Simplify code by implementing the walrus operator in Python 3.8+

while (n:=int(input())) != -1:
    time = 0
    distance = 0

    for i in range(n):
        mph,h = map(int, input().split())
        distance += (h - time) * mph
        time = h
    print(distance, "miles")
