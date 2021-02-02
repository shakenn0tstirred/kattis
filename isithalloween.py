# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

date = input().split()

if date[0] == "OCT" and date[1] == "31" or date[0] == "DEC" and date[1] == "25":
    print("yup")
else:
    print("nope")
