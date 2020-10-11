for i in range(int(input())): # Loop through each set of guests
    guests = int(input()) # Don't actually need number of guests
    guest_numbers = input().split()
    for j in guest_numbers: # Go though each invitation number
        if guest_numbers.count(j) == 1: # Check for unmatched invitation
            print("Case #" + str(i+1) + ":",j) # If invitation is unmatched, it's the odd one out
            break # End the loop after odd one out is found
