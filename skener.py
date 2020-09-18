rows, columns, new_rows, new_columns = map(int, input().split())

for i in range(rows):
    line = list(input())

    line = [ele for ele in line for j in range(new_columns)]
    
    for k in range(new_rows):
        print("".join(line))
