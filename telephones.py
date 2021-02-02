# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

N, M = map(int, input().split())

while N != 0 and M != 0:
    call_log = list()
    
    for i in range(N):
        source, destination, start, duration = map(int, input().split())

        duration += start
        
        for j in range(start, duration):
            call_log.append(j)
    
    for k in range(M):
        operators = 0
        start, duration = map(int, input().split())
        duration += start

        for l in range(start, duration):

            if call_log.count(l) > operators:
                operators = call_log.count(l)
        else:
            print(operators)

    N, M = map(int, input().split())
