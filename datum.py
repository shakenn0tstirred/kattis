from calendar import weekday

D,M = map(int, input().split())
answer = weekday(2009,M,D)
if answer == 0:
    answer = "Monday"
elif answer == 1:
    answer = "Tuesday"
elif answer == 2:
    answer = "Wednesday"
elif answer == 3:
    answer = "Thursday"
elif answer == 4:
    answer = "Friday"
elif answer == 5:
    answer = "Saturday"
else:
    answer = "Sunday"

print(answer)
