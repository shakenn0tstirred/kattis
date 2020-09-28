for i in range(int(input())):
    command = input()
    if "Simon says" in command:
        print(command[11:])
