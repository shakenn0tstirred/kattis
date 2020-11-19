line = input().split()

while line != ['0','0']:
    line[0] = int(line[0])
    line[1] = int(line[1])
    
    print(line[0]//line[1],line[0]%line[1],'/',line[1])
    line = input().split()
