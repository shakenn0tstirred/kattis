# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import pi 
radius = int(input())

# The Euclidian area of a circle is (pi)(radius**2)
print((radius ** 2) * pi)

# The taxicab area is essentially the area of a square with each edge equaling the radius, doubled
print((radius ** 2) * 2)
