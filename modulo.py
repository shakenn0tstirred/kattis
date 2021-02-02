# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

numbers = [] # Initialize the input list

# Use list comprehension to sort through the input
numbers += [int(input()) % 42 for i in range(10)]
print(len(set(numbers)))
