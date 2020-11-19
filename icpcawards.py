winners = list()
rank = 0

for _ in range(int(input())):
    school,team = input().split()
    if school not in winners:
        print(school,team)
        winners.append(school)
        rank+=1
    if rank == 12:
        break
