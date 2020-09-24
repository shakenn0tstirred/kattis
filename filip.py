A, B = input().split() # Input two numbers as strings

# Reverse both strings, convert into integer
A = int(A[::-1])
B = int(B[::-1])

# Compare the integers and print the largest one
if A > B:
    print(A)
else:
    print(B)
