# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for i in range(int(input())):
    trips = int(input())
    cities = []
    
    for j in range(trips): # Create list of all of the cities
        cities.append(input())
    # Since sets remove duplicates, its length is equal to its unique elements
    print(len(set(cities)))
