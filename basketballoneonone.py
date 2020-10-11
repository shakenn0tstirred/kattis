# Initialize team scores
a = 0
b = 0

for i in input():
    if i.isdigit(): # If the character is a score, add it to the correct team's score
        if team == "A":
            a += int(i)
        else:
            b += int(i)
    else: # If the character is a team, note which team scored
        team = i
# Print the team with the highest score
if a > b: 
    print("A")
else:
    print("B")
