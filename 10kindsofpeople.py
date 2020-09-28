r, c = map(int, input().split())
rows = list()
query = []

for i in range(r):
    rows.append(input())

n = int(input())

for j in range(n):
    query = "".join(input().split()) # Need to remove whitespace between numbers

    # Need to decrement by 1 (and cast to int) to obtain true index location
    x1 = int(query[0]) - 1
    y1 = int(query[1]) - 1
    x2 = int(query[2]) - 1
    y2 = int(query[3]) - 1
    
    if rows[x1][y1] == "0" and rows[x2][y2] == "0":
        print("binary")
    elif rows[x1][y1] == "1" and rows[x2][y2] == "1":
        print("decimal")
    else: # If the two coordinates are different
        print("neither")
    
    # x1, y1 == rows[query[0]][query[1]]
    # x2, y2 == rows[query[2]][query[3]]


    
##    query[0] == x1 == row/line of x1,y1
##    query[1] == y1 == column/char of x1,y1
##    query[2] == x2 == row/line of x2,y2
##    query[3] == y2 == column/char of x2,y2
##
##
## Obvi, if x1,y1 == x2,y2, then it can be binary or decimal, but
## if x1,y1 != x2,y2, then it must be "neither" - default to neither
