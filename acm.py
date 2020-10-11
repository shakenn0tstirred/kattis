attempt = input().split()

# Initialize variables
problems = []
score = 0
num_correct = 0

while len(attempt) != 1: # All inputs save for the last have a length of 3, so this could also be written as "while len(attempt) == 3"
    
   time = int(attempt[0])
   problem = attempt[1]
   status = attempt[2]

   if status == "wrong": # If the problem is wrong, add its problem number to the running list
      problems.append(problem)

   if status == "right": # If the problem is right, increment num_correct and add its time to the score
      score += time
      num_correct += 1
      if problems.count(problem) != 0: # If the problem had been wrong previously, a penalty time is incurred
         score += problems.count(problem) * 20 # Add to score: number of wrong attempts multiplied by 20

   attempt = input().split()

print(num_correct,score)
