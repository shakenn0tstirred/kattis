# Kattis-accepted version
for i in range(int(input())):
    command = input()
    if "Simon says" in command:
        print(command[11:])

# Simplified version introduced in Python 3.8
for i in range(int(input())):
    if "Simon says" in (command:=input()):
        print(command[11:])
