# Kattis-accepted code
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x > 0:
    print(4)
elif y > 0:
    print(2)
else:
    print(3)
    
    
# Simplified version utilizing the walrus operator introduced in Python 3.8

if (x:=int(input())) > 0 and (y:=int(input())) > 0:
    print(1)
elif x > 0:
    print(4)
elif y > 0:
    print(2)
else:
    print(3)
