name = input()
new_name = "" # This will be our name

for i in name:
    if len(new_name) != 0:
        if i != letter: # If the letter isn't the same as the one before, add to the output name
            letter = i
            new_name +=i
    else: # If it's the first letter, add it to the ouput name
        letter = i
        new_name += i
print(new_name)
