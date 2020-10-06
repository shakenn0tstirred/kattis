answer = 0
for _ in range(int(input())):
    color = input()

    if "rose" in color.lower() or "pink" in color.lower():
        answer+=1


if answer == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(answer)
