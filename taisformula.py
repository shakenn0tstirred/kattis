# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

trapezoid = 0.0 #Initialize running total

for i in range(int(input())):
    if i == 0: # Initialize starting value
        initial = input().split()
        milliseconds_initial = int(initial[0])
        glucose_initial = float(initial[1])
    else:
        current = input().split()
        milliseconds_current = int(current[0])
        glucose_current = float(current[1])
        
        # Use given formula to calculate area of the trapezoid
        trapezoid_current = glucose_current + glucose_initial
        trapezoid_current /= 2
        trapezoid_current *= milliseconds_current - milliseconds_initial
        trapezoid += trapezoid_current # Add derived area to running total
        
        # Set initial value to current total
        milliseconds_initial = milliseconds_current
        glucose_initial = glucose_current
else:
    print(trapezoid/1000) # Convert milliseconds to seconds upon printing running total
