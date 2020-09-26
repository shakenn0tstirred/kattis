name = input()
shortname = list()
for letter in name:
    if letter.isupper() == True:
        shortname.append(letter)
print("".join(shortname))
