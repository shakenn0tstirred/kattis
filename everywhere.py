T = int(input())

for i in range(T):
    trips = int(input())
    cities = []
    
    for j in range(trips): # Create list of all of the cities
        cities.append(input())
    # Since sets remove duplicates, its length is equal to its unique elements
    print(len(set(cities)))