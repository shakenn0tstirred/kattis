politicians = list()
votes = list()
answer = list()

for _ in range(int(input())):
    candidate = input()
    party = input()
    politicians.append([party,candidate])

for _ in range(int(input())):
    votes.append(input())

votes.sort()

for sublist in politicians:
    tally = 0
    for name in votes:
        if name == sublist[1]:
            tally+=1
    answer.append([tally,sublist[0]])

answer.sort(reverse = True)
if answer[0][0] == answer[1][0]:
  print("tie")
else:
  print(answer[0][1])
