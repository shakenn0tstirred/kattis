for i in range(int(input())):
  #Initialize starting variables
  initial_turtle = 0
  answer = 0
  for k,j in enumerate(input().split()):
      if int(j) == 0: # Stop when number of turtles is 0
          break
      if k != 0:
          if int(j) > initial_turtle: # Checks to see if island had any immigrants
              answer += int(j) - initial_turtle # Add number of turtle immigrants
      initial_turtle = int(j) * 2 # Set lower growth limit for next cycle
      print(answer)
