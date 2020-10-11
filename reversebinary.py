N = bin(int(input())) # Convert input to binary
N = N[2:]             # Remove 0b from beginning of number
N = N[::-1]           # Reverse number
print(int(N,2))       # Convert number to decimal
