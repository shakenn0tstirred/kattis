# Get input for given variables
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

p /= 100  # Convert percentage to decimal
i = 0     # Index counter
T = t[i]  # Add first segment to running total
j = i + 1 # Shorthand since i+1 is used so much

if t[i] == k or p == 0 or p == 100: 
    pass  # If the video doesn't speed up, skip the else statement
else:
    while j < n: # Adding the segments to the running total
        T = T + (1 + p*j) * (t[j] - t[i])
        i+=1
        j+=1

T = T + (1 + p*j) * (k - t[i]) # Needed to add the last segment to the running total
print(T)
