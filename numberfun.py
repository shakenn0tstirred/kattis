# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for i in range(int(input())):
    answer = "Impossible"
    a,b,c = map(int, input().split())
    
    if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
        answer = "Possible"
        
    print(answer)
