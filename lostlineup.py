num_people = int(input())
people = input().split()
original_order = []

for i,k in enumerate(people):
    original_order.append([int(k),i+2])
original_order.sort()

answer = "1"
for k in range(len(original_order)):
    answer += " " + str(original_order[k][1])
print(answer)
