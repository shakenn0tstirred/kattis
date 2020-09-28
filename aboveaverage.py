C = int(input())              # C is the number of test cases/data set inputs to follow
i = 0                         # set index to zero
while i < C:                  # Since C starts at 1 and i starts at 0, this will amount in C input cases
    grades = list(map(int, input().split()))
    N = grades[0]             # Keep the number of students
    del grades[0]             # Delete number of students from list of final grades
    average = sum(grades) / N # Compute class average
    
    for x in grades[:]:
        if x < average or x == average:
            del grades[grades.index(x)]
    aboveAverage = len(grades) / N # Compute percentage of students that scored above average
    print("{:.3%}".format(aboveAverage))
    i += 1
