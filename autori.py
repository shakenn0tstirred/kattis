shortname = list()
for letter in input():
    if letter.isupper() == True:
        shortname.append(letter)
print("".join(shortname))
