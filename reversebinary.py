# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

N = bin(int(input())) # Convert input to binary
N = N[2:]             # Remove 0b from beginning of number
N = N[::-1]           # Reverse number
print(int(N,2))       # Convert number to decimal
