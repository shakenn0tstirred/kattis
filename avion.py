# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

answer = ""

if "FBI" in input():
    answer += "1"
if "FBI" in input():
    answer += "2"
if "FBI" in input():
    answer += "3"
if "FBI" in input():
    answer += "4"
if "FBI" in input():
    answer += "5"

if len(answer) != 0:
    print(" ".join(answer))
else:
    print("HE GOT AWAY!")
