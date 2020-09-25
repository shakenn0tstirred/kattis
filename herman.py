from math import pi 
radius = int(input())

# The Euclidian area of a circle is (pi)(radius**2)
print((radius ** 2) * pi)

# The taxicab area is essentially the area of a square with each edge equaling the radius, doubled
print((radius ** 2) * 2)
