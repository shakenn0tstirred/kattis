for i in range(int(input())): # Iterate through given number of students
    grades = list(map(int, input().split()))
    N = grades[0]             # Keep the number of students
    del grades[0]             # Delete number of students from list of final grades
    average = sum(grades) / N # Compute class average
    
    for x in grades[:]:
        if x < average or x == average:
            del grades[grades.index(x)]
    aboveAverage = len(grades) / N # Compute percentage of students that scored above average
    print("{:.3%}".format(aboveAverage))
