from math import pi
line = input().split()


while line != ['0', '0', '0']:
    r = float(line[0])
    m = int(line[1])
    c = int(line[2])
    d = 2 * r

    print(pi*r**2,(c/m)*d**2)
    
    line = input().split()
