# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math
# Go through each test case
for i in range(int(input())):
  x = 0
  y = 0
  heading = 0
  distance = 0
  
  for j in range(int(input())): # Go through each command
    
    direction, command = input().split() # Input both parts of the command
    command = int(command) # Cast number into int

    # Recode possible input strings into something that makes more sense
    backward = "bk"
    foreward = "fd"
    left = "lt"
    right = "rt"

    if direction == foreward:
        tempX = command * math.cos(math.radians(heading)) # Use cosine to find turtle's X coordinate
        tempY = command * math.sin(math.radians(heading)) # Use sine to find turtle's Y coordinate
        x += tempX
        y += tempY
    elif direction == backward:
        command *= -1 # Reverse the command to maintain header angle
        tempX = command * math.cos(math.radians(heading)) # Use cosine to find turtle's X coordinate
        tempY = command * math.sin(math.radians(heading)) # Use sine to find turtle's Y corrdinate
        x += tempX
        y += tempY
    elif direction == left:
        heading = (heading + command) % 360 # keep number between 0 and 360; add because piviting left is positive
    elif direction == right:
        heading = (heading - command) % 360 # Ensure a negative direction is between 0 and 360; since turning right is negative, need to subtract the command to maintain turtle's true heading rather than its relative heading
  distance = math.sqrt(x**2 + y**2)
  print(round(distance))
