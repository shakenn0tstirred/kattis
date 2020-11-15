for i in range(int(input())):
    r, e, c = map(int, input().split())

    cost = e - c
    if r < cost:
        print("advertise")
    elif r > cost:
        print("do not advertise")
    else:
        print("does not matter")
