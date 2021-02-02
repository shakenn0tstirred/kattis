# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

line = input().split()

while line != ['0','0']:
    line[0] = int(line[0])
    line[1] = int(line[1])
    
    print(line[0]//line[1],line[0]%line[1],'/',line[1])
    line = input().split()
