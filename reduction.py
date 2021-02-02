# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

for i in range(int(input())):
    N, M, L = map(int, input().split())
    agency_list = list() # Need to keep track of each agency

    for j in range(L):
        agencyname, cash = input().split(':') # Seperate agency's name from its prices
        A, B = map(int, cash.split(',')) # Seperate the cash string into A and B
        min_price = 0 # Initialize min_price
        n = N # Need a temporary N (n) so we retain the intial value of N
        
        while n != M:
            # What these next lines do is compare the price ratio of A and B, 
            # and figure out what N would be if either halved or if reduced by 1
            halved = n//2

            if halved < M:
                min_price += (n - M)*A
                n = M
            else:
                price_B = B
                price_A = (n-halved)*A
                if price_B < price_A:
                    min_price += price_B
                    n = halved
                else:
                    min_price += price_A
                    n = halved
            
        else: # This runs after the while loop ends, and appends output to list
            agency_list.append(agencyname + " " + str(min_price))
    # This sorts the list by numbers first then by the agency name
    agency_list.sort(key = lambda ele: (int(ele.split()[1]), str.lower(ele)))
    
    print("Case " + str(i+1))

    for element in agency_list:
        print(element)
