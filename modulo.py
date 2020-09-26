numbers = [] # Initialize the input list

# Use list comprehension to sort through the input
numbers += [int(input()) % 42 for i in range(10)]
print(len(set(numbers)))
