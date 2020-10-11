days = []

for i in range(int(input())):
    s,t = map(int,input().split()) # Get two dates
    days += range(s,t+1) # Add covered dates to list
print(len(set(days))) #Sets remove duplicates, so print number of non-duplicate days
