# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

A, B = input().split() # Input two numbers as strings

# Reverse both strings, convert into integer
A = int(A[::-1])
B = int(B[::-1])

# Compare the integers and print the largest one
if A > B:
    print(A)
else:
    print(B)
