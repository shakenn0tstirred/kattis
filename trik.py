# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def move_A(ball_position):
    if ball_position == 1:
        return 2
    elif ball_position == 2:
        return 1
    return 3

def move_B(ball_position):
    if ball_position == 2:
        return 3
    elif ball_position == 3:
        return 2
    return 1

def move_C(ball_position):
    if ball_position == 1:
        return 3
    elif ball_position == 3:
        return 1
    return 2

position = 1
for char in input():
    if char == "A":
        position = move_A(position)
    elif char == "B":
        position = move_B(position)
    else: #if char == "C"
        position = move_C(position)
print(position)
