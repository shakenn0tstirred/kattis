colors = []
for i in range(int(input())):
    cups = input().split()
    
    if cups[0].isdigit(): # If the first string is a number, it's a diameter and the color is second
        colors.append([int(cups[0])/2, cups[1]]) # Save as list of radius (radius = diameter/2), color
    else: # The first element in this input is a color, so the second element is a radius
        colors.append([int(cups[1]), cups[0]]) # Save as list of radius, color

colors.sort() # Sort colors from smallest radius to largest radius
for j in range(len(colors)): # Print colors (stored as second element in each nested list) in order
    print(colors[j][1])
