for i in range(int(input())):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        a,b = line.split('+') # .split() defaults to splitting a string at a space, so split the line at the plus sign
        print(int(a) + int(b)) # Output the added numbers
