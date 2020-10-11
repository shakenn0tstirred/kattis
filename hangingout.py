L, x = map(int,input().split())
groups = 0
terrace = 0

for i in range(x):
    people = input().split()
    if people[0] == "enter":
        total = int(people[1]) + terrace # Set total to be equal to people[1] + people on terrace
        if total <= L: # If people entering would be under or equal to terrace capacity
            terrace += int(people[1])
        else: # If people entering would exceed terrace capacity, reject them and increment group count
            groups += 1
    else: # If people[0] == "leave":
        terrace -= int(people[1]) # Remove people[1] people from the terrace count

print(groups) # Print number of rejected groups
