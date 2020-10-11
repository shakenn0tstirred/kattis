P,N = map(int, input().split())
parts = set()

for i in range(N):
    parts.add(input()) # Add part to set of parts
    if len(parts) == P: # If the sailor has replaced all of the parts, print the date
        print(i+1)
        break
else: # If the sailor hasn't replaced all of the boat's part, print "paradox avoided"
    print("paradox avoided")
