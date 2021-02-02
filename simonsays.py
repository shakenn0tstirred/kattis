# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Kattis-accepted version
for i in range(int(input())):
    command = input()
    if "Simon says" in command:
        print(command[11:])

# Simplified version introduced in Python 3.8
for i in range(int(input())):
    if "Simon says" in (command:=input()):
        print(command[11:])
