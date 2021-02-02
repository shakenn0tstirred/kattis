# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

rows, columns, new_rows, new_columns = map(int, input().split())

for i in range(rows):
    line = list(input())

    line = [ele for ele in line for j in range(new_columns)]
    
    for k in range(new_rows):
        print("".join(line))
